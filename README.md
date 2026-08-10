<p align="center">
  <img src="assets/banner.png" alt="VECTRA_MACHIN" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ROS-2-00e5ff?style=for-the-badge&logo=ros&logoColor=black" />
  <img src="https://img.shields.io/badge/Python-3.10+-ffd23f?style=for-the-badge&logo=python&logoColor=black" />
  <img src="https://img.shields.io/badge/OpenCV-Vision-7dffb3?style=for-the-badge&logo=opencv&logoColor=black" />
  <img src="https://img.shields.io/badge/AI-Multimodal-ff5fb0?style=for-the-badge" />
  <img src="https://img.shields.io/badge/status-arquitetura%2Fdesign-8f7bff?style=for-the-badge" />
  <img src="https://img.shields.io/badge/license-MIT-3a8fff?style=for-the-badge" />
</p>

<h1 align="center">🧠 VECTRA_MACHIN</h1>

<p align="center">
  <b>🇺🇸 <a href="#-english">English</a> &nbsp;|&nbsp; 🇧🇷 <a href="#-português">Português</a></b>
</p>

---

## 🇺🇸 English

### 📌 Description

**VECTRA_MACHIN** is a **Multimodal AI architecture for autonomous robotic
systems**. The goal is a system capable of turning information from
different sensors and human commands into autonomous decisions and actions.

The core flow is a continuous loop:

<p align="center">
  <img src="assets/loop.png" alt="Perception-Decision-Action loop" width="60%">
</p>

```
Perception → Understanding → World Model → Decision
    → Navigation → Action → Feedback → Adaptation → Perception
```

The project combines environment perception, semantic representation,
decision-making, planning and adaptation into a single modular pipeline.

### 🎯 Objectives

- Integrate multiple sources of information
- Interpret visual and sensor data
- Detect objects and obstacles
- Build a representation of the environment
- Relate human goals to elements in the environment
- Turn abstract goals into spatial goals
- Perform navigation planning
- Use feedback to adapt behavior
- Provide a modular architecture for autonomous systems

### 🧠 Architecture

<p align="center">
  <img src="assets/modules.png" alt="Module architecture" width="65%">
</p>

Each block is an independent module with a clear responsibility, connected
through a shared world representation rather than direct point-to-point
coupling — any module can be replaced (a different perception model, a
different planner) without breaking the rest of the pipeline.

### 👁️ Perception

Turns raw sensor data into information the other modules can use.

**Sources:** camera, LiDAR, IMU, odometry.

**Outputs:** objects, obstacles, terrain, free space, depth, motion, position.

The architecture is designed to later plug in computer-vision models such
as object detection, segmentation, depth estimation, tracking, scene
recognition and sensor fusion.

### 🌎 World Model

Maintains an up-to-date representation of the environment, gathering
everything perception produces into a shared structure:

```
World Model
│
├── Robot State
│   ├── Position
│   ├── Orientation
│   └── Velocity
│
├── Objects
├── Obstacles
├── Terrain
├── Semantic Locations
├── Dynamic Entities
└── Uncertainty
```

This shared structure lets every downstream module reason over the same
view of the world.

### 🗣️ Vision + Language

One of the project's key features: relating natural language to visual
perception. For example:

> "Go to the free area near the door."

The system can interpret this as:

```
target: free_area
reference: door
relation: near
```

That structured intent is then grounded against the door's detected
position in the environment:

```
LANGUAGE + VISION → SPATIAL MEANING
```

This lets abstract human commands become concrete goals the navigation
system can act on.

### 🧭 Navigation

Once a decision is made, navigation turns the goal into a trajectory:

```
World Model
     ↓
Global Planner
     ↓
Local Planner
     ↓
Obstacle Avoidance
     ↓
Trajectory
```

The architecture is designed to plug in different planning algorithms —
including the RT-RRT approach explored in a companion project — as one of
several possible planning strategies within this pipeline.

### 🔄 Adaptation

A feedback-based adaptation layer keeps the system from depending solely
on a previously computed trajectory:

```
Action → Movement → Feedback → Comparison → Error → Adaptation → New action
```

It can account for terrain changes, dynamics shifts, slippage, unexpected
obstacles, localization error, mismatches between expected and actual
motion, and changes in actuator response.

### 🛡️ Safety

An independent safety layer sits between decision-making and the robot:

```
Decision → Navigation → Motor Adaptation → Safety → Robot
```

It can constrain speed, minimum obstacle distance, dangerous commands and
emergency situations — keeping intelligent decision-making separate from
hard safety constraints.

### 📂 Project structure

```
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
```

### ⚙️ Technologies

- Python · ROS 2 · OpenCV · NumPy
- Computer Vision · Multimodal AI
- Trajectory planning · Sensor fusion · World modeling

Designed for future integration with: YOLO, Vision Transformers,
Vision-Language Models, depth estimation models, SLAM, and reinforcement
learning.

### 🚀 Running

**1. Build the workspace**

```bash
cd ~/projeto2_ws
colcon build --symlink-install
source install/setup.bash
```

**2. Launch**

```bash
ros2 launch projeto2_robot projeto2.launch.py
```

**3. Check nodes**

```bash
ros2 node list
```

**4. Check topics**

```bash
ros2 topic list
```

### 📡 Main modules

| Module | Function |
|---|---|
| `perception_node.py` | Environment perception |
| `world_model_node.py` | World representation |
| `decision_node.py` | Goal interpretation and decision-making |
| `navigation_node.py` | Planning |
| `motor_adaptation_node.py` | Feedback-based adaptation |
| `safety_node.py` | Safety constraints |
| `main_controller.py` | Overall coordination |

### 🔬 Example run

User input: *"Go to the free area near the door."*

```
1. Receive the goal
        ↓
2. Analyze sensor data
        ↓
3. Detect the door
        ↓
4. Update the World Model
        ↓
5. Interpret "free area near"
        ↓
6. Create a spatial goal
        ↓
7. Plan a trajectory
        ↓
8. Execute the action
        ↓
9. Receive feedback
        ↓
10. Adapt behavior
```

### 🆚 Compared to the companion RT-RRT project

| RT-RRT project | VECTRA_MACHIN |
|---|---|
| RT-RRT | Multimodal AI |
| Planning | Perception + decision |
| Trajectory | Goal + trajectory + action |
| Geometry | Geometry + semantics |
| Dynamic environment | Environment + meaning |
| Planner | World Model |
| Replanning | Replanning + adaptation |

The RT-RRT project focuses on the trajectory-planning problem itself.
VECTRA_MACHIN broadens the scope to understanding and autonomy — covering
perception, language, world representation, decision-making, planning and
adaptation.

### 🎯 Expected outcome

A modular architecture representing the full cycle:

```
Perception → Understanding → World Representation → Decision
    → Planning → Action → Feedback → Adaptation → New Perception
```

A foundation for autonomous robotic systems capable of understanding their
environment, interpreting human goals, and adapting their behavior.

### 📄 License

MIT — see `LICENSE` for details.

---

## 🇧🇷 Português

### 📌 Descrição

O **VECTRA_MACHIN** apresenta uma **arquitetura de Inteligência Artificial
Multimodal para sistemas robóticos autônomos**. O objetivo é um sistema
capaz de transformar informações de diferentes sensores e comandos humanos
em decisões e ações autônomas.

O fluxo principal é um ciclo contínuo:

<p align="center">
  <img src="assets/loop.png" alt="Ciclo Percepção-Decisão-Ação" width="60%">
</p>

```
Percepção → Compreensão → World Model → Decisão
    → Navegação → Ação → Feedback → Adaptação → Percepção
```

O projeto combina percepção do ambiente, representação semântica, tomada
de decisão, planejamento e adaptação em um único pipeline modular.

### 🎯 Objetivos

- Integrar diferentes fontes de informação
- Interpretar informações visuais e sensoriais
- Detectar objetos e obstáculos
- Construir uma representação do ambiente
- Relacionar objetivos humanos com elementos do ambiente
- Transformar objetivos abstratos em objetivos espaciais
- Realizar planejamento de navegação
- Utilizar feedback para adaptar o comportamento
- Criar uma arquitetura modular para sistemas autônomos

### 🧠 Arquitetura

<p align="center">
  <img src="assets/modules.png" alt="Arquitetura de módulos" width="65%">
</p>

Cada bloco é um módulo independente com responsabilidade clara, conectado
através de uma representação compartilhada do mundo em vez de acoplamento
direto ponto a ponto — qualquer módulo pode ser substituído (um modelo de
percepção diferente, um planejador diferente) sem quebrar o restante do
pipeline.

### 👁️ Percepção

Transforma dados brutos dos sensores em informação útil para os demais
módulos.

**Fontes:** câmera, LiDAR, IMU, odometria.

**Saídas:** objetos, obstáculos, terreno, espaço livre, profundidade,
movimento, posição.

A arquitetura permite futuramente conectar modelos de visão computacional
como detecção de objetos, segmentação, estimativa de profundidade,
tracking, reconhecimento de cenas e fusão de sensores.

### 🌎 World Model

Mantém uma representação atualizada do ambiente, reunindo tudo que a
percepção produz em uma estrutura comum:

```
World Model
│
├── Robot State
│   ├── Position
│   ├── Orientation
│   └── Velocity
│
├── Objects
├── Obstacles
├── Terrain
├── Semantic Locations
├── Dynamic Entities
└── Uncertainty
```

Essa estrutura compartilhada permite que todos os módulos seguintes
raciocinem sobre a mesma visão do mundo.

### 🗣️ Visão + Linguagem

Uma das principais características do projeto: relacionar linguagem
natural com percepção visual. Por exemplo:

> "Vá até a área livre próxima à porta."

O sistema pode interpretar isso como:

```
target: free_area
reference: door
relation: near
```

Essa intenção estruturada é então relacionada com a posição da porta
detectada no ambiente:

```
LINGUAGEM + VISÃO → SIGNIFICADO ESPACIAL
```

Isso permite que comandos humanos abstratos se tornem objetivos concretos
que o sistema de navegação pode executar.

### 🧭 Navegação

Depois que a decisão é tomada, a navegação transforma o objetivo em uma
trajetória:

```
World Model
     ↓
Global Planner
     ↓
Local Planner
     ↓
Obstacle Avoidance
     ↓
Trajectory
```

A arquitetura é pensada para permitir a integração de diferentes
algoritmos de planejamento — incluindo a abordagem RT-RRT explorada em um
projeto complementar — como um dos métodos possíveis de planejamento
dentro deste pipeline.

### 🔄 Adaptação

Uma camada de adaptação baseada em feedback evita que o sistema dependa
exclusivamente de uma trajetória calculada anteriormente:

```
Ação → Movimento → Feedback → Comparação → Erro → Adaptação → Nova ação
```

Ela pode considerar mudanças no terreno, alteração da dinâmica,
escorregamento, obstáculos inesperados, erro de localização, diferença
entre movimento esperado e realizado, e alteração na resposta dos
atuadores.

### 🛡️ Segurança

Uma camada de segurança independente fica entre a tomada de decisão e o
robô:

```
Decision → Navigation → Motor Adaptation → Safety → Robot
```

Ela pode limitar velocidade, distância mínima de obstáculos, comandos
perigosos e situações de emergência — separando a tomada de decisão
inteligente das restrições de segurança.

### 📂 Estrutura do projeto

```
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
```

### ⚙️ Tecnologias

- Python · ROS 2 · OpenCV · NumPy
- Visão Computacional · IA Multimodal
- Planejamento de trajetória · Sensor Fusion · World Modeling

Pensado para integração futura com: YOLO, Vision Transformers,
Vision-Language Models, modelos de profundidade, SLAM e aprendizado por
reforço.

### 🚀 Execução

**1. Compilar o projeto**

```bash
cd ~/projeto2_ws
colcon build --symlink-install
source install/setup.bash
```

**2. Executar**

```bash
ros2 launch projeto2_robot projeto2.launch.py
```

**3. Verificar os nós**

```bash
ros2 node list
```

**4. Verificar os tópicos**

```bash
ros2 topic list
```

### 📡 Principais módulos

| Módulo | Função |
|---|---|
| `perception_node.py` | Percepção do ambiente |
| `world_model_node.py` | Representação do mundo |
| `decision_node.py` | Interpretação e decisão |
| `navigation_node.py` | Planejamento |
| `motor_adaptation_node.py` | Adaptação baseada em feedback |
| `safety_node.py` | Segurança |
| `main_controller.py` | Coordenação geral |

### 🔬 Exemplo de funcionamento

Entrada do usuário: *"Vá até a área livre próxima à porta."*

```
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
```

### 🆚 Diferença em relação ao projeto RT-RRT complementar

| Projeto RT-RRT | VECTRA_MACHIN |
|---|---|
| RT-RRT | IA multimodal |
| Planejamento | Percepção + decisão |
| Trajetória | Objetivo + trajetória + ação |
| Geometria | Geometria + semântica |
| Ambiente dinâmico | Ambiente + significado |
| Planner | World Model |
| Replanejamento | Replanejamento + adaptação |

O projeto RT-RRT concentra-se principalmente no problema de planejamento
de trajetória. O VECTRA_MACHIN amplia o escopo para compreensão e
autonomia, considerando percepção, linguagem, representação do mundo,
decisão, planejamento e adaptação.

### 🎯 Resultado esperado

Uma arquitetura modular representando o ciclo completo:

```
Percepção → Compreensão → Representação do Mundo → Decisão
    → Planejamento → Ação → Feedback → Adaptação → Nova Percepção
```

Uma base para o desenvolvimento de sistemas robóticos autônomos capazes de
compreender o ambiente, interpretar objetivos humanos e adaptar seu
comportamento.

### 📄 Licença

MIT — veja `LICENSE` para mais detalhes.

---

<p align="center">
  <sub>Perception · World Model · Decision · Navigation · Adaptation · Safety</sub>
</p>
