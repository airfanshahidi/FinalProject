# Game Flowchart

Below is the flowchart representing the main components and flow of the game:

```flow
graph TD;
    A[Start] --> B[Main Menu]
    B -->|Start Game| C[Initialize Player]
    B -->|View Instructions| D[Show Instructions]
    B -->|Exit| E[End Game]
    C --> F[Game Loop]
    F --> G[Display Map]
    G --> H[Player Move]
    H --> I[Check for Encounter]
    I -->|Encounter| J[Battle System]
    J --> K[Update Player/Opponent HP]
    K --> L[Check Battle Outcome]
    L -->|Win| M[Update Player Stats]
    L -->|Lose| N[End Game]
    L -->|Continue| O[Return to Map]
    O --> F