using System.ComponentModel.DataAnnotations;

namespace apiProdutos;

public class produto
{
    [Key]
    public int ID { get; set; }
    [Required]
    [MaxLength(100)]

    public string nome { get; set; } = String.Empty;
    [Required]
    [MaxLength(500)]

    public string descricao { get; set; } = string.Empty;

    [Required]
    public decimal preco { get; set; }
    
    [Required] 
    public int estoque { get; set; }

    public DateTime DataCriacao { get; set; } = DateTime.Now;
}