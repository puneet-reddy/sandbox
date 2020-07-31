using Microsoft.EntityFrameworkCore;
using webapi_csharp.Models;

namespace webapi_csharp.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext (DbContextOptions<AppDbContext> options)
            : base(options)
        {
        }

        public DbSet<AppFile> File { get; set; }
    }
}