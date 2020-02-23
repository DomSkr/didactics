using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using CRUD_EXAMPLE.Data;
using CRUD_EXAMPLE.Models;

namespace CRUD_EXAMPLE.Controllers
{
    public class OpiniasController : Controller
    {
        private readonly OpiniaContext _context;

        public OpiniasController(OpiniaContext context)
        {
            _context = context;
        }

        // GET: Opinias
        public async Task<IActionResult> Index()
        {
            return View(await _context.Opinia.ToListAsync());
        }

        // GET: Opinias/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var opinia = await _context.Opinia
                .FirstOrDefaultAsync(m => m.ID == id);
            if (opinia == null)
            {
                return NotFound();
            }

            return View(opinia);
        }

        // GET: Opinias/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Opinias/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("ID,Rate,Comment,Nickname")] Opinia opinia)
        {
            if (ModelState.IsValid)
            {
                _context.Add(opinia);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(opinia);
        }

        // GET: Opinias/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var opinia = await _context.Opinia.FindAsync(id);
            if (opinia == null)
            {
                return NotFound();
            }
            return View(opinia);
        }

        // POST: Opinias/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("ID,Rate,Comment,Nickname")] Opinia opinia)
        {
            if (id != opinia.ID)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(opinia);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!OpiniaExists(opinia.ID))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(opinia);
        }

        // GET: Opinias/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var opinia = await _context.Opinia
                .FirstOrDefaultAsync(m => m.ID == id);
            if (opinia == null)
            {
                return NotFound();
            }

            return View(opinia);
        }

        // POST: Opinias/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var opinia = await _context.Opinia.FindAsync(id);
            _context.Opinia.Remove(opinia);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool OpiniaExists(int id)
        {
            return _context.Opinia.Any(e => e.ID == id);
        }
    }
}
