# VECTRA_MACHIN
📌 Descrição

O Projeto 2 apresenta uma arquitetura de Inteligência Artificial Multimodal para sistemas robóticos autônomos.

O objetivo é desenvolver um sistema capaz de transformar informações provenientes de diferentes sensores e comandos humanos em decisões e ações autônomas.

A arquitetura principal segue o fluxo:

Percepção
    ↓
Compreensão
    ↓
World Model
    ↓
Decisão
    ↓
Navegação
    ↓
Ação
    ↓
Feedback
    ↓
Adaptação
    ↓
Percepção

O projeto combina percepção do ambiente, representação semântica, tomada de decisão, planejamento e adaptação.

🎯 Objetivos

O projeto tem como principais objetivos:

integrar diferentes fontes de informação;
interpretar informações visuais e sensoriais;
detectar objetos e obstáculos;
construir uma representação do ambiente;
relacionar objetivos humanos com elementos do ambiente;
transformar objetivos abstratos em objetivos espaciais;
realizar planejamento de navegação;
utilizar feedback para adaptar o comportamento;
criar uma arquitetura modular para sistemas autônomos.
🧠 Arquitetura

A arquitetura do sistema é dividida em diferentes módulos:

                         HUMAN / GOAL
                              │
                              ▼
                    ┌──────────────────┐
                    │   DECISION AI    │
                    │                  │
                    │ interpretação    │
                    │ de objetivos     │
                    └────────┬─────────┘
                             │
                             ▼
┌──────────┐          ┌──────────────────┐
│  Camera  │─────────►│                  │
├──────────┤          │    PERCEPTION    │
│  LiDAR   │─────────►│                  │
├──────────┤          │ objetos          │
│   IMU    │─────────►│ obstáculos       │
├──────────┤          │ terreno          │
│ Odometry │─────────►│ movimento        │
└──────────┘          └────────┬─────────┘
                               │
                               ▼
                      ┌──────────────────┐
                      │    WORLD MODEL   │
                      │                  │
                      │ Robot State      │
                      │ Objects          │
                      │ Obstacles        │
                      │ Terrain          │
                      │ Locations        │
                      │ Uncertainty      │
                      └────────┬─────────┘
                               │
                               ▼
                      ┌──────────────────┐
                      │    NAVIGATION    │
                      │                  │
                      │ Global Planning  │
                      │ Local Planning   │
                      │ Avoidance        │
                      └────────┬─────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ MOTOR ADAPTATION    │
                    │                     │
                    │ Action              │
                    │ Feedback            │
                    │ Adaptation          │
                    └──────────┬──────────┘
                               │
                               ▼
                         ┌───────────┐
                         │   SAFETY  │
                         └─────┬─────┘
                               │
                               ▼
                             ROBÔ
                               │
                               │ Feedback
                               ▼
                         WORLD MODEL
👁️ Percepção

O módulo de percepção é responsável por transformar dados dos sensores em informações úteis para os demais módulos.

As principais fontes consideradas são:

câmera;
LiDAR;
IMU;
odometria.

A percepção pode fornecer informações como:

Objetos
Obstáculos
Terreno
Espaço livre
Profundidade
Movimento
Posição

A arquitetura permite posteriormente adicionar modelos de visão computacional, como:

detecção de objetos;
segmentação;
estimativa de profundidade;
tracking;
reconhecimento de cenas;
fusão de sensores.
🌎 World Model

O World Model mantém uma representação atualizada do ambiente.

Ele reúne as informações provenientes da percepção em uma estrutura comum.

Exemplo:

World Model
│
├── Robot State
│   ├── Position
│   ├── Orientation
│   └── Velocity
│
├── Objects
│
├── Obstacles
│
├── Terrain
│
├── Semantic Locations
│
├── Dynamic Entities
│
└── Uncertainty

Essa representação permite que os diferentes módulos utilizem uma mesma visão do ambiente.

🗣️ Visão + Linguagem

Uma das principais características do projeto é a possibilidade de relacionar linguagem com percepção visual.

Por exemplo:

"Vá até a área livre próxima à porta."

O sistema pode interpretar:

target: free_area

reference: door

relation: near

A informação é então relacionada com a posição da porta detectada no ambiente.

O objetivo é transformar:

LINGUAGEM
    +
VISÃO
    ↓
SIGNIFICADO ESPACIAL

Isso permite que comandos abstratos sejam convertidos em objetivos que podem ser utilizados pelo sistema de navegação.

🧭 Navegação

Depois que a decisão é tomada, o módulo de navegação transforma o objetivo em uma trajetória.

World Model
     │
     ▼
Global Planner
     │
     ▼
Local Planner
     │
     ▼
Obstacle Avoidance
     │
     ▼
Trajectory

O sistema também pode ser integrado posteriormente a diferentes algoritmos de planejamento.

Entre eles está o conceito utilizado no Projeto 1, como o RT-RRT, que pode ser utilizado como um dos métodos de planejamento dentro desta arquitetura.

🔄 Adaptação

O sistema possui uma camada de adaptação baseada em feedback.

O fluxo é:

Ação
  ↓
Movimento
  ↓
Feedback
  ↓
Comparação
  ↓
Erro
  ↓
Adaptação
  ↓
Nova ação

A adaptação pode considerar situações como:

mudança no terreno;
alteração da dinâmica;
escorregamento;
obstáculos inesperados;
erro de localização;
diferença entre movimento esperado e realizado;
alteração na resposta dos atuadores.

Dessa forma, o sistema não depende exclusivamente de uma trajetória calculada anteriormente.

🛡️ Segurança

A arquitetura também possui uma camada independente de segurança.

Decision
   ↓
Navigation
   ↓
Motor Adaptation
   ↓
Safety
   ↓
Robot

A camada de segurança pode limitar:

velocidade;
distância mínima de obstáculos;
comandos perigosos;
situações de emergência.

Isso permite separar a tomada de decisão inteligente das restrições de segurança.

📂 Estrutura do projeto
projeto2_robot/
│
├── config/
│   └── robot.yaml
│
├── launch/
│   └── projeto2.launch.py
│
├── resource/
│   └── projeto2_robot
│
├── projeto2_robot/
│   ├── __init__.py
│   ├── decision_node.py
│   ├── main_controller.py
│   ├── motor_adaptation_node.py
│   ├── navigation_node.py
│   ├── perception_node.py
│   ├── safety_node.py
│   └── world_model_node.py
│
├── README.md
├── package.xml
├── setup.cfg
└── setup.py
⚙️ Tecnologias

O projeto foi estruturado para utilizar:

Python
ROS 2
OpenCV
NumPy
Visão Computacional
IA Multimodal
Planejamento de trajetória
Sensor Fusion
World Modeling

A arquitetura também permite integração futura com modelos como:

YOLO;
Vision Transformers;
Vision-Language Models;
modelos de profundidade;
SLAM;
aprendizado por reforço.
🚀 Execução
1. Compilar o projeto

Na workspace ROS 2:

cd ~/projeto2_ws

colcon build --symlink-install

Depois:

source install/setup.bash
2. Executar
ros2 launch projeto2_robot projeto2.launch.py
3. Verificar os nós
ros2 node list
4. Verificar os tópicos
ros2 topic list
📡 Principais módulos
Módulo	Função
perception_node.py	Percepção do ambiente
world_model_node.py	Representação do mundo
decision_node.py	Interpretação e decisão
navigation_node.py	Planejamento
motor_adaptation_node.py	Adaptação baseada em feedback
safety_node.py	Segurança
main_controller.py	Coordenação geral
🔬 Exemplo de funcionamento

O usuário fornece:

"Vá até a área livre próxima à porta."

O sistema executa:

1. Recebe o objetivo
        ↓
2. Analisa os sensores
        ↓
3. Detecta a porta
        ↓
4. Atualiza o World Model
        ↓
5. Interpreta "área livre próxima"
        ↓
6. Cria um objetivo espacial
        ↓
7. Planeja uma trajetória
        ↓
8. Executa a ação
        ↓
9. Recebe feedback
        ↓
10. Adapta o comportamento
🆚 Diferença em relação ao Projeto 1
Projeto 1	Projeto 2
RT-RRT	IA multimodal
Planejamento	Percepção + decisão
Trajetória	Objetivo + trajetória + ação
Geometria	Geometria + semântica
Ambiente dinâmico	Ambiente + significado
Planner	World Model
Replanejamento	Replanejamento + adaptação

O Projeto 1 concentra-se principalmente no problema de planejamento de trajetória.

O Projeto 2 amplia o problema para compreensão e autonomia, considerando percepção, linguagem, representação do mundo, decisão, planejamento e adaptação.

🎯 Resultado esperado

Ao final, o sistema possui uma arquitetura capaz de representar o ciclo:

Percepção
    ↓
Compreensão
    ↓
Representação do Mundo
    ↓
Decisão
    ↓
Planejamento
    ↓
Ação
    ↓
Feedback
    ↓
Adaptação
    ↓
Nova Percepção

Essa arquitetura representa uma base para o desenvolvimento de sistemas robóticos autônomos capazes de compreender o ambiente, interpretar objetivos e adaptar seu comportamento.
