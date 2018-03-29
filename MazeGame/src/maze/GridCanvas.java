package maze;

import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.Image;

class GridCanvas extends Canvas {
	private static final long serialVersionUID = -8222465479781205354L;
	Graphics graphicsBuffer;
	private Image imageBuffer;
    Image[] images;
	final int BASE_SIZE = 10;
	private final int CELL_EDGE = 16;
    private final int UNKNOWN = 0;
    private final int OPEN = 1;
    private final int WALL = 2;
    private final int PLAYER = 3;
        
    GridCanvas(Image[] images) {
    	this.images = images;
    }
	
	public void repaint() { //inherited, can't drop from public
		paint(this.getGraphics());
	}
	
	public void update(Graphics g) { //inherited, can't drop from public
		paint(g);
	}

	public void paint(Graphics g) {
		if(graphicsBuffer == null) {
			imageBuffer = createImage(getTotalWidth(),getTotalHeight());
			graphicsBuffer = imageBuffer.getGraphics();
		}
		displayGrid(graphicsBuffer);
		g.drawImage(imageBuffer,0,0,this);
	}	
    
    private void displayGrid(Graphics g) {
		for(int i = 0; i < MazeWindow.grid.size[0]; i++) {
			for(int j = 0; j < MazeWindow.grid.size[1]; j++) {
				if ((i == MazeWindow.thePlayer.getPosition()[0]) && (j == MazeWindow.thePlayer.getPosition()[1])) {
					g.drawImage(images[PLAYER], j * CELL_EDGE, i * CELL_EDGE, null);
				}
				else {
					g.drawImage(images[(MazeWindow.grid.played[i][j]) ? ((MazeWindow.grid.theGrid[i][j].checkHere()) ? OPEN : WALL) : UNKNOWN], j * CELL_EDGE, i * CELL_EDGE, null);
				}				
			}
		}
	}
	
	int getTotalWidth() {
		return MazeWindow.grid.size[1] * CELL_EDGE;
	}

	int getTotalHeight() {
		return MazeWindow.grid.size[0] * CELL_EDGE;
	}
}