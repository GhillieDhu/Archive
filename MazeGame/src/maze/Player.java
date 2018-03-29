package maze;

class Player {
    private int[] position = new int[2];
    private int steps;
    
    Player () {}
    
    void placeAtEntry(int entry) {
        position[0] = 0;
        position[1] = entry;
        steps = 0;
    }
    
    int[] getPosition() {
        return position;
    }
    
    void moveUp() {
        position[0]--;
        steps++;
    }
    
    void moveDown() {
        position[0]++;
        steps++;
    }
    
    void moveRight() {
        position[1]++;
        steps++;
    }
    
    void moveLeft() {
        position[1]--;
        steps++;
    }
    
    int getPlayerSteps() {
    	return steps;
    }
}