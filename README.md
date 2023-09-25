# **Análise de reputação com base em comentários no Twitter**

*As redes sociais são espaços na Internet que permitem a criação e compartilhamento de conteúdo, sendo fontes importantes de informações e opiniões. A indústria cinematográfica é uma das que se beneficia das redes sociais, pois são utilizadas como meios de divulgação de filmes e fontes de opiniões que podem influenciar e entender o comportamento dos usuários.* 



### Arquitetura

![Arquitetura](https://imgur.com/IpUuqfl)

`Etapa 1:` Extração dos dados web no Twitter utilizando técnica de WebScraping executada na ferramenta Jupyter Notebook em computador On-Premises.

`Etapa 2:` Ingestão dos dados brutos com origem On-Premises para destino em Cloud utilizando Azure Data Factory.

`Etapa 3:` Armazenamento do arquivo bruto na ferramenta de Data Lake Azure Data Lake Storage e transformação do arquivo utilizando Python.

`Etapa 4:` Processamento in cloud do arquivo bruto limpando os dados e transformando utilizando o recurso Azure Databricks com processamento em cluster.

`Etapa 5:` Visualização do resultado da etapa anterior com Microsoft Power BI.



### Metodologia

Para coletar os dados do twitter, sobre as opiniões dos usuários da plataforma de streaming Netflix, utilizaremos o processo de extração web Scraping, que é muito utilizado em estratégias de transformação digital, bem como para automatizar processos de coleta e consulta de dados.
Inicialmente pensamos na utilização da API (Interface de Programação de Aplicações), como os dados do Twitter são comumente usados para fins de marketing e pesquisa, a documentação da API possui limitações de acesso e um alto custo de utilização, por este motivo, optamos pelo desenvolvimento do web scraper que permite a criação da nossa própria API, que pode ser vinculada a qualquer site ou plataforma.
Para realização desta extração utilizaremos a aplicação Jupyter Notebook, para a criação da web scraping, que fará a raspagem dos dados que desejamos coletar da rede social Twitter.



### Web Scraping

Foi desenvolvido, na IDE do Jupyter Notebook, um código em Python para a realização da raspagem de dados, metodologia também conhecida como Web Scraping. Com isso, será possível extrair Twitters da página oficial do Twitter com a hashtag #NetflixBrasil, com datas de corte de 03/09/2022 até 03/01/2023, tendo em vista que o plano de assinatura básico da Netflix foi implantado em 03/11/2022 foi definido dois meses depois e antes dessa data para avaliar os Twitters.



*Todo o conteúdo está no arquivo em PDF dentro deste repositório.*
