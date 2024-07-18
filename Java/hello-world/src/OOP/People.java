package OOP;

import java.math.BigInteger;

public class People {
  private String nome;
  private String sobrenome;
  private String nomeCompleto;
  private  long telefone;
  public People(String nome, String sobrenome, long telefone) {
    setNome(nome);
    setSobrenome(sobrenome);
    setTelefone(telefone);
  }
  
  public void setNome(String nome) {
    this.nome = nome.trim();
  }
  
  public void setSobrenome(String sobrenome) {
    this.nome = sobrenome.trim();
  }
  
  public void setTelefone(long telefone) {
    this.telefone = telefone;
  }
  
  public void setNomeCompleto() {
    if(this.nome != null & this.sobrenome != null) {
      this.nomeCompleto = this.nome.concat(String.format(" %d", sobrenome));
    }
  }
  
  public String getNome() {
    return nome;
  }
  
  public String getSobrenome() {
    return sobrenome;
  }
  
  public String getNomeCompleto() {
    return nomeCompleto;
  }
  
  public long getTelefone() {
    return telefone;
  }
}
