using apiProdutos;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi
builder.Services.AddOpenApi();

builder.Services.AddDbContext<AppDbContext>(options => options.UseSqlite("Data Source = produtos.Db"));


var app = builder.Build();
app.MapGet("/produtos", (AppDbContext db) =>
{
    var produtos = db.Produtos.ToList();
    
    return  Results.Ok(produtos);
});

app.MapGet("/produtos/{id}", (AppDbContext db, int id) =>
{

    var produto = db.Produtos.Find(id);

    return produto != null ? Results.Ok(produto) : Results.NotFound();
});
app.MapPost("/produtos", (AppDbContext db, produto produto) =>
{
    db.Produtos.Add(produto);
    db.SaveChanges();
    return Results.Created($"/produtos/{produto.ID}", produto);
});

app.MapDelete("/produtos/{id}", (AppDbContext db, int id) =>
{
    var produto = db.Produtos.Find(id);
    if (produto == null) return Results.NotFound();
    db.Produtos.Remove(produto);
    db.SaveChanges();
    return Results.NoContent();
});

app.MapPut("/produtos/{id}", (AppDbContext db, int id, produto produto) =>
{
    if(id != produto.ID) return Results.BadRequest();
    db.Entry(produto).State = EntityState.Modified;
    db.SaveChanges();
    return Results.NoContent();
});

//Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();


app.Run();

