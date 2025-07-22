🛰️ Projeto Star Wars

Este projeto pessoal simula um mini data lake baseado no universo de Star Wars, utilizando ferramentas de baixo custo da AWS.

🎯 Objetivo

Construir um pipeline de ingestão, transformação e consulta de dados utilizando APIs públicas e serviços AWS, com visualização via Power BI.

🛠️ Tecnologias Utilizadas

**Python**: coleta de dados da API [SWAPI](https://swapi.dev/)
**Pandas**: tratamento e exportação para CSV
**Amazon S3**: armazenamento dos dados em data lake
**AWS Glue + Lake Formation**: catálogo de dados e permissões
**Amazon Athena**: consultas SQL no data lake
**Power BI**: visualização dos dados

🗂️ Estrutura do Projeto

<img width="240" height="410" alt="image" src="https://github.com/user-attachments/assets/dc60b10d-0d1e-47e0-a3bf-4a30362bf5ef" />


<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/ee8bad0e-47fd-4cad-9821-03f8eca1103b" />

🚀 Próximos Passos (envolve custos)

- Automatizar coleta via Lambda + CloudWatch
- Adicionar monitoramento (SNS)
