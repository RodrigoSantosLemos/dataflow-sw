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

dataflow-sw/
├── data/
│   ├── processed/              
│   └── raw/                    
│
├── doc/                        
│
├── scripts/                    
│   ├── extract-swapi-films.py
│   ├── extract-swapi-people.py
│   ├── extract-swapi-planets.py
│   ├── extract-swapi-species.py
│   ├── extract-swapi-starships.py
│   └── extract-swapi-vehicles.py
│
├── sql/                        
│
├── glue_starwars_policy_full.json     
├── glue-inline-policy.json            
├── glue-trust-policy.json             
│
├── .gitignore
├── README.md
└── requirements.txt (opcional)


<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/ee8bad0e-47fd-4cad-9821-03f8eca1103b" />

🚀 Próximos Passos (envolve custos)
Automatizar coleta via Lambda + CloudWatch
Adicionar monitoramento (SNS)
