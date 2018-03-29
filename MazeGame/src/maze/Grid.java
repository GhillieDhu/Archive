package maze;

import java.util.Random;

class Grid{
	
	static final int GAME_DIFFICULTY_BEGINNER = 0;
	static final int GAME_DIFFICULTY_INTERMEDIATE = 1;
	static final int GAME_DIFFICULTY_EXPERT = 2;
	static final int GAME_DIFFICULTY_CUSTOM = 3;
	static final int BASE_SIZE = 10;
    
	Cell[][] theGrid;
    boolean[][] played;
	int[] size = new int[2];
    int entry;
	
    private int exit;
	private int steps;
    private int boardHeight = BASE_SIZE * 2;
    private int boardWidth = BASE_SIZE * 3;
	    
    Grid() {
    	initializeGrid();
    }
    
    private void initializeGrid() {
    	Random generator = new Random();
    	size[0] = boardHeight;
        size[1] = boardWidth;
        entry = Math.abs(generator.nextInt()) % (size[1] - 2) + 1;
    	exit = Math.abs(generator.nextInt(entry)) % (size[1] - 2) + 1;
        int iterations = 0;
        theGrid = new Cell[size[0]][size[1]];
        played = new boolean[size[0]][size[1]];
        for (int i = 0; i < size[0]; i++) {
        	theGrid[i][0] = new Cell("edge");
        	played[i][0] = true;
        	theGrid[i][size[1] - 1] = new Cell("edge");
        	played[i][size[1] - 1] = true;
        }
        for (int j = 1; j < size[1] - 1; j++) {
        	if (j == entry) theGrid[0][j] = new Cell("door");
        	else theGrid[0][j] = new Cell("edge");
        	played[0][j] = true;
        	if (j == exit) theGrid[size[0] - 1][j] = new Cell("door");
        	else theGrid[size[0] - 1][j] = new Cell("edge");
        	played[size[0] - 1][j] = true;
        }
        for (int i = 1; i < size[0] - 1; i++)
            for (int j = 1; j < size[1] - 1; j++) {
            	theGrid[i][j] = new Cell("middle");
            	played[i][j] = false;
            }
        while (!passable()) {
            for (int i = 1; i < size[0] - 1; i++)
                for (int j = 1; j < size[1] - 1; j++)
                	theGrid[i][j].regenerate();
        	iterations++;
        }
        played[1][entry] = true;
        MazeWindow.thePlayer.placeAtEntry(entry);
    }
    
    void setSize(int height, int width) throws IllegalArgumentException {
    	if ((width < 3) || (height < 3)) {
    		throw new IllegalArgumentException("Size must exceed 2");
    	}
    	boardWidth = width;
    	boardHeight = height;

		MazeWindow.gridCanvas.graphicsBuffer = null;
		initializeGrid();
		MazeWindow.gridCanvas.setSize(MazeWindow.gridCanvas.getTotalWidth(),MazeWindow.gridCanvas.getTotalHeight());
		MazeWindow.gridCanvas.repaint();
	}

    void newGame() {
		setSize(boardHeight,boardWidth);
	}
    
    boolean passable() {
        steps = 0;
        int[] checker = new int[2];
        checker[0] = 0;
        checker[1] = entry;
        char direction = 'D';
        do {
           switch (direction) {
               case 'L':
	                   if (theGrid[checker[0] - 1][checker[1]].checkHere()) {
	                       checker[0]--;
	                       direction = 'U';
	                   }
	                   else if (theGrid[checker[0]][checker[1] - 1].checkHere()) {
	                       checker[1]--;
	                       direction = 'L';
	                   }
	                   else if (theGrid[checker[0] + 1][checker[1]].checkHere()) {
	                       checker[0]++;
	                       direction = 'D';
	                   }
	                   else {
	                       checker[1]++;
	                       direction = 'R';
	                   }
	                   steps++;
               break;
               case 'D':
	                   if (theGrid[checker[0]][checker[1] - 1].checkHere()) {
	                       checker[1]--;
	                       direction = 'L';
	                   }
	                   else if (theGrid[checker[0] + 1][checker[1]].checkHere()) {
	                       checker[0]++;
	                       direction = 'D';
	                   }
	                   else if (theGrid[checker[0]][checker[1] + 1].checkHere()) {
	                       checker[1]++;
	                       direction = 'R';
	                   }
	                   else if (checker[0] != 0) { //guard condition for if first space past opening is blocked
	                       checker[0]--;
	                       direction = 'U';
	                   }
	                   else break;
	                   steps++;
               break;
               case 'R':if (theGrid[checker[0] + 1][checker[1]].checkHere()) {
	                       checker[0]++;
	                       direction = 'D';
	                   }
	                   else if (theGrid[checker[0]][checker[1] + 1].checkHere()) {
	                       checker[1]++;
	                       direction = 'R';
	                   }
	                   else if (theGrid[checker[0] - 1][checker[1]].checkHere()) {
	                       checker[0]--;
	                       direction = 'U';
	                   }
	                   else {
	                       checker[1]--;
	                       direction = 'L';
	                   }
	                   steps++;
               break;
               case 'U':if (theGrid[checker[0]][checker[1] + 1].checkHere()) {
	                       checker[1]++;
	                       direction = 'R';
	                   }
	                   else if (theGrid[checker[0] - 1][checker[1]].checkHere()) {
	                       checker[0]--;
	                       direction = 'U';
	                   }
	                   else if (theGrid[checker[0]][checker[1] - 1].checkHere()) {
	                       checker[1]--;
	                       direction = 'L';
	                   }
	                   else {
	                       checker[0]++;
	                       direction = 'D';
	                   }
	                   steps++;
               break;
           }
        } while (checker[0] > 0 && checker[0] < (size[0] - 1));
        boolean isPassable = (checker[0] > 0);
        if (isPassable) {
        	int stepsThere = steps;
            steps = 0;
            direction = 'U';
            do {
                switch (direction) {
                    case 'L':
     	                   if (theGrid[checker[0] - 1][checker[1]].checkHere()) {
     	                       checker[0]--;
     	                       direction = 'U';
     	                   }
     	                   else if (theGrid[checker[0]][checker[1] - 1].checkHere()) {
     	                       checker[1]--;
     	                       direction = 'L';
     	                   }
     	                   else if (theGrid[checker[0] + 1][checker[1]].checkHere()) {
     	                       checker[0]++;
     	                       direction = 'D';
     	                   }
     	                   else {
     	                       checker[1]++;
     	                       direction = 'R';
     	                   }
     	                   steps++;
                    break;
                    case 'D':
     	                   if (theGrid[checker[0]][checker[1] - 1].checkHere()) {
     	                       checker[1]--;
     	                       direction = 'L';
     	                   }
     	                   else if (theGrid[checker[0] + 1][checker[1]].checkHere()) {
     	                       checker[0]++;
     	                       direction = 'D';
     	                   }
     	                   else if (theGrid[checker[0]][checker[1] + 1].checkHere()) {
     	                       checker[1]++;
     	                       direction = 'R';
     	                   }
     	                   else {
     	                       checker[0]--;
     	                       direction = 'U';
     	                   }
     	                   steps++;
                    break;
                    case 'R':if (theGrid[checker[0] + 1][checker[1]].checkHere()) {
     	                       checker[0]++;
     	                       direction = 'D';
     	                   }
     	                   else if (theGrid[checker[0]][checker[1] + 1].checkHere()) {
     	                       checker[1]++;
     	                       direction = 'R';
     	                   }
     	                   else if (theGrid[checker[0] - 1][checker[1]].checkHere()) {
     	                       checker[0]--;
     	                       direction = 'U';
     	                   }
     	                   else {
     	                       checker[1]--;
     	                       direction = 'L';
     	                   }
     	                   steps++;
                    break;
                    case 'U':if (theGrid[checker[0]][checker[1] + 1].checkHere()) {
     	                       checker[1]++;
     	                       direction = 'R';
     	                   }
     	                   else if (theGrid[checker[0] - 1][checker[1]].checkHere()) {
     	                       checker[0]--;
     	                       direction = 'U';
     	                   }
     	                   else if (theGrid[checker[0]][checker[1] - 1].checkHere()) {
     	                       checker[1]--;
     	                       direction = 'L';
     	                   }
     	                   else {
     	                       checker[0]++;
     	                       direction = 'D';
     	                   }
     	                   steps++;
                    break;
                }
            } while (checker[0] > 0 && checker[0] < (size[0] - 1));
            steps = (steps < stepsThere ? steps : stepsThere);
        }
        return isPassable;
    }
    
    int score() {
    	return size[0] * size[1] * (steps - MazeWindow.thePlayer.getPlayerSteps()) / steps;
    }
}