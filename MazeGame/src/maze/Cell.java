package maze;

import java.util.Random;

class Cell {
    private boolean open;
    Random generator = new Random();
    static int modulator = 2;
    
    Cell(String force) {
        if (force == "edge") {
        	open = false;
        }
        else if (force == "door") {
        	open = true;
        }
        else {
            this.regenerate();
        }
    }
    
    void regenerate() {
    	open = (generator.nextInt() % modulator != 0);
    }
    
    boolean checkHere() {
        return open;
    }
}