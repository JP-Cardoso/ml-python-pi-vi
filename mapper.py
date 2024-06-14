class MapperData:
  @staticmethod
  def mapper(dados) -> dict:
      data = {
        "conta": {
          "idConta": dados["idConta"]
        },
        "dados": {
          "ID": 0,
          "genero": dados["genero"],
          "carro_proprio": dados["carro_proprio"],
          "casa_propria": dados["casa_propria"],
          "filhos": dados["filhos"],
          "tipo_de_renda": dados["tipo_de_renda"],
          "grau_de_escolaridade": dados["grau_de_escolaridade"],
          "estado_civil": dados["estado_civil"],
          "tipo_de_moradia": dados["tipo_de_moradia"],
          "celular": dados["celular"],
          "telefone_trabalho": dados["telefone_trabalho"],
          "telefone": dados["telefone"],
          "email": dados["email"],
          "membros_da_familia": dados["membros_da_familia"],
          "faixa_etaria": dados["faixa_etaria"],
          "renda_anual": dados["renda_anual"],
          "tempo_emprego": dados["tempo_emprego"],
          "tempo_registro_dados":dados["tempo_registro_dados"]            
        }
      }
      return data
