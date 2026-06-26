# Regras do Projeto (Workspace Rules)

1. **Ciclo de Especificação:** Sempre que o usuário estiver falando sobre geração de especificação ou idealização de algo, a Inteligência Artificial deve acessar e ler primeiro o arquivo `specs/README.md`, que contém o protocolo geral e direciona a leitura dos demais arquivos (como o ciclo de vida e a especificação ativa).
2. **Registro de Prompts:** Todo e qualquer prompt enviado pelo usuário nesta workspace deve ser obrigatoriamente registrado no arquivo `prompts.jsonl` na raiz da workspace, contendo o ID incremental, o timestamp do prompt, o ID da conversa atual, o texto exato do prompt e metadados úteis (como tags de contexto).
3. **Registro e Leitura de Contexto:** Todo e qualquer passo, decisão principal e resumo de pensamento da IA deve ser registrado resumidamente no arquivo `context.jsonl` na raiz da workspace. Ao iniciar um novo chat, a Inteligência Artificial deve ler este arquivo para se alinhar com o progresso atual, decisões tomadas e tarefas pendentes.


