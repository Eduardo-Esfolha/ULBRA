using Microsoft.EntityFrameworkCore;

namespace apiProdutos;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
    {
        
    }

    public DbSet<produto> Produtos { get; set; }
    
    
}