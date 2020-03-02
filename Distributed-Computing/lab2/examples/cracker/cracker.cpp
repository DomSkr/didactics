/*
 *       Parallel Password Cracker with OpenMP
 *       Compile: g++ cracker.cpp -fopenmp -lcrypto -std=c++11 -o pwcracker
 */
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <openssl/sha.h>
#include <openssl/md5.h>
#include <omp.h>

std::string computeHash_SHA512(std::string input);
std::string computeHash_MD5(std::string input);
std::string singleHashingRound(int round_number, std::string input);
char * tryHax(char * input);

void chop(char * word) {
  int lenword = strlen(word);
  if(word[lenword - 2] == ' ' || word[lenword - 2] == '\n' || word[lenword - 2] == '\r' || word[lenword - 2] == '\t') {
     word[lenword - 2] = '\0';
  }
  if(word[lenword - 1] == ' ' || word[lenword - 1] == '\n' || word[lenword - 1] == '\r' || word[lenword - 1] == '\t') {
    word[lenword - 1] = '\0';
  }
}

int numlines(FILE * file) {
  if (file == NULL) {
    return -1;
  }

  char ch;
  int lines = 0;
  while (ch != EOF) {
    ch = fgetc(file);
    if (ch == '\n') {
      lines++;
    }
  }
  return lines;
}

char word[BUFSIZ], salt[BUFSIZ], pwhash[BUFSIZ];

int main(int argc, char * argv[]) {
  //Parameters error handling
  if (argc != 4) {
    printf("Parallel Password Cracker\nUSAGE: ./pwcracker <PATH TO DICTIONARY> <SHA-512 HASH> <SALT>'\n");
    exit(-1);
  }

  int found = 0; //0 = password not found ; 1 = password found

  FILE * words = fopen(argv[1], "r"); //Open dictionary file
  //File error handling
  if (words == NULL) {
    printf("Cannot open dictionary file.\n");
    exit(-1);
  }

  strcpy(salt, argv[3]);
  strcpy(pwhash, argv[2]);
  int size = numlines(words); // Number of words in dictionary

  //seek error handling
  if (fseek(words, 0, SEEK_SET) == -1) {
    exit(-1);
  }

  //Parallel Region
  # pragma omp parallel for private(word) shared(found) schedule(dynamic)
  for (int i = 0; i < size; i++) {
    if (fgets(word, BUFSIZ, words) != NULL) {
      chop(word);
      if (found == 1) {
        exit(1);
      }
      printf("[*] THREAD %i TRYING: %s\n", omp_get_thread_num(), word);
      char * hash = tryHax(word);
      if (strcmp(hash, pwhash) == 0) {
        printf("[+] PASSWORD FOUND: %s\n", word);
        found = 1;
      }
    }
  }

  fclose(words);
  if (found == 0) {
    printf("[-] PASSWORD NOT FOUND, EXITING...\n");
  }

  return 0;
}

char * tryHax(char * input) {
  std::string result = input;

  for (int i = 0; i < 100000; i++) {
    result = singleHashingRound(i + 1, result);
  }

  return (char * ) result.c_str();
}

std::string singleHashingRound(int round_number, std::string input) {
  if (round_number == 1) {
    /* We'll keeping the unsalted MD5 + SHA512 as the first hashing
     * round, for backward compatibility. (This makes it possible to
     * add salt to existing hashes without knowing the correct
     * passwords.) */
    return computeHash_SHA512(computeHash_MD5(input));
  } else {
    /* All the other rounds are salted. */
    return computeHash_SHA512(input + salt);
  }
}

std::string computeHash_SHA512(std::string string) {
  unsigned char digest[SHA512_DIGEST_LENGTH];

  SHA512_CTX ctx;
  SHA512_Init( & ctx);
  SHA512_Update( & ctx, string.c_str(), string.length());
  SHA512_Final(digest, & ctx);

  char mdString[SHA512_DIGEST_LENGTH * 2 + 1];
  for (int i = 0; i < SHA512_DIGEST_LENGTH; i++) {
    sprintf( & mdString[i * 2], "%02x", (unsigned int) digest[i]);
  }
  return mdString;
}

std::string computeHash_MD5(std::string string) {
  unsigned char digest[16];

  MD5_CTX ctx;
  MD5_Init( & ctx);
  MD5_Update( & ctx, string.c_str(), string.length());
  MD5_Final(digest, & ctx);

  char mdString[33];
  for (int i = 0; i < 16; i++) {
    sprintf( & mdString[i * 2], "%02x", (unsigned int) digest[i]);
  }
  return mdString;
}
