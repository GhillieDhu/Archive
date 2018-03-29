package maze;

import java.awt.CheckboxMenuItem;
import java.awt.Frame;
import java.awt.Image;
import java.awt.Menu;
import java.awt.MenuBar;
import java.awt.MenuItem;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

class MazeWindow extends Frame implements WindowListener, ActionListener, ItemListener, KeyListener {
	private static final long serialVersionUID = 3351350507397080308L;
	static Grid grid;
	static GridCanvas gridCanvas;
	private CheckboxMenuItem menuGameTypes[];
	private int currentGameDifficulty;
	private MenuItem newGame;
	private MenuItem quitGame;
	private MazeGameDialog customField;
	private ScoreDialog score;
	static Player thePlayer;

	MazeWindow() {
		super("aMAZEing");
	}
	
	void init(Image[] images) {
		setupMenus();
		addKeyListener(this);
		thePlayer = new Player();
		grid = new Grid();
		gridCanvas = new GridCanvas(images);
		addWindowListener(this);
		add(gridCanvas);
		pack();
		setSize(gridCanvas.getTotalWidth(),gridCanvas.getTotalHeight());//plus the height of the menu...
		gridCanvas.setSize(gridCanvas.getTotalWidth() + getInsets().left + getInsets().right,
				gridCanvas.getTotalHeight()+ getInsets().top + getInsets().bottom);
		setSize(gridCanvas.getTotalWidth() + getInsets().left + getInsets().right,
				gridCanvas.getTotalHeight()+ getInsets().top + getInsets().bottom);
		setVisible(true);
		gridCanvas.setVisible(true);
		setGameDifficulty(Grid.GAME_DIFFICULTY_BEGINNER);
		setResizable(false);
	}
	
	private void setupMenus() {
		MenuBar menuBar = new MenuBar();
		Menu menu = new Menu("Game");
		newGame = new MenuItem("New Game");
		quitGame = new MenuItem("Quit");
		newGame.addActionListener(this);
		quitGame.addActionListener(this);
		menu.add(newGame);
		menu.add("-");
		menuGameTypes = new CheckboxMenuItem[4];
		menuGameTypes[Grid.GAME_DIFFICULTY_BEGINNER] = new CheckboxMenuItem("Beginner");
		menu.add(menuGameTypes[Grid.GAME_DIFFICULTY_BEGINNER]);
		menuGameTypes[Grid.GAME_DIFFICULTY_INTERMEDIATE] = new CheckboxMenuItem("Intermediate");
		menu.add(menuGameTypes[Grid.GAME_DIFFICULTY_INTERMEDIATE]);
		menuGameTypes[Grid.GAME_DIFFICULTY_EXPERT] = new CheckboxMenuItem("Expert");
		menu.add(menuGameTypes[Grid.GAME_DIFFICULTY_EXPERT]);
		menuGameTypes[Grid.GAME_DIFFICULTY_CUSTOM] = new CheckboxMenuItem("Custom...");
		menu.add(menuGameTypes[Grid.GAME_DIFFICULTY_CUSTOM]);
		menuGameTypes[Grid.GAME_DIFFICULTY_BEGINNER].addItemListener(this);
		menuGameTypes[Grid.GAME_DIFFICULTY_INTERMEDIATE].addItemListener(this);
		menuGameTypes[Grid.GAME_DIFFICULTY_EXPERT].addItemListener(this);
		menuGameTypes[Grid.GAME_DIFFICULTY_CUSTOM].addItemListener(this);
		menu.add(new CheckboxMenuItem("-"));
		menu.add(quitGame);
		menuBar.add(menu);
		setMenuBar(menuBar);
	}
	
	private void kill() {
		dispose();
	}

	public void windowClosing(WindowEvent e) {
		kill();
	}

	public void actionPerformed(ActionEvent e) {
		if (e.getSource().equals(newGame)) {
			grid.newGame();
		}
		else if(e.getSource().equals(quitGame)) {
			kill();
		}
	}

	public void itemStateChanged(ItemEvent e) {
		CheckboxMenuItem menuitem = (CheckboxMenuItem)(e.getItemSelectable());
		if(menuitem == menuGameTypes[Grid.GAME_DIFFICULTY_BEGINNER]) {
			setGameDifficulty(Grid.GAME_DIFFICULTY_BEGINNER);
		}
		else if (menuitem == menuGameTypes[Grid.GAME_DIFFICULTY_INTERMEDIATE]) {
			setGameDifficulty(Grid.GAME_DIFFICULTY_INTERMEDIATE);
		}
		else if (menuitem == menuGameTypes[Grid.GAME_DIFFICULTY_EXPERT]) {
				setGameDifficulty(Grid.GAME_DIFFICULTY_EXPERT);
		}
		else {
			customField = new MazeGameDialog(this,grid.size[0], grid.size[1]);
			customField.setVisible(true);
			setGameDifficulty(Grid.GAME_DIFFICULTY_CUSTOM);
		}
		gridCanvas.graphicsBuffer = null;
		gridCanvas.repaint();
		setSize(gridCanvas.getTotalWidth() + getInsets().left + getInsets().right, gridCanvas.getTotalHeight()+ getInsets().top + getInsets().bottom);
	}

	private void setGameDifficulty(int newGameDifficulty) {
		switch (newGameDifficulty) {
			case 0: grid.setSize(Grid.BASE_SIZE * 2,Grid.BASE_SIZE * 3);
	    	break;
			case 1: grid.setSize(Grid.BASE_SIZE * 3,Grid.BASE_SIZE * 9 / 2);
			break;
			case 2: grid.setSize(Grid.BASE_SIZE * 4,Grid.BASE_SIZE * 6);
			break;
			case 3: grid.setSize(customField.getHeight(),customField.getWidth());
			break;
			default:
				throw new IllegalArgumentException("Error: Game difficulty "+"setting must be between 0 and "+(menuGameTypes.length -1)+", not "+newGameDifficulty);
			}
		menuGameTypes[currentGameDifficulty].setState(false);
		currentGameDifficulty = newGameDifficulty;
		menuGameTypes[currentGameDifficulty].setState(true);
	}

	public void keyPressed(KeyEvent e) {
		if (MazeWindow.thePlayer.getPosition()[0] < grid.size[0] - 1) {
			int id = e.getKeyCode();
	        switch (id) {
	        case KeyEvent.VK_LEFT:
	            if (grid.theGrid[MazeWindow.thePlayer.getPosition()[0]][MazeWindow.thePlayer.getPosition()[1] - 1].checkHere()) {
	                MazeWindow.thePlayer.moveLeft();
	            	grid.played[MazeWindow.thePlayer.getPosition()[0]][MazeWindow.thePlayer.getPosition()[1] - 1] = true;
	            	grid.played[MazeWindow.thePlayer.getPosition()[0] - 1][MazeWindow.thePlayer.getPosition()[1]] = true;
	            	grid.played[MazeWindow.thePlayer.getPosition()[0] + 1][MazeWindow.thePlayer.getPosition()[1]] = true;
	            }
	            gridCanvas.repaint();
	            break;
	        case KeyEvent.VK_UP:
	        	if (MazeWindow.thePlayer.getPosition()[0] > 0) {
	        		if (grid.theGrid[MazeWindow.thePlayer.getPosition()[0] - 1][MazeWindow.thePlayer.getPosition()[1]].checkHere()) {
        				MazeWindow.thePlayer.moveUp();
		            	grid.played[MazeWindow.thePlayer.getPosition()[0] - 1][MazeWindow.thePlayer.getPosition()[1]] = true;
		            	grid.played[MazeWindow.thePlayer.getPosition()[0]][MazeWindow.thePlayer.getPosition()[1] - 1] = true;
		            	grid.played[MazeWindow.thePlayer.getPosition()[0]][MazeWindow.thePlayer.getPosition()[1] + 1] = true;
		            }
	        	}
	            gridCanvas.repaint();
	            break;
	        case KeyEvent.VK_RIGHT:
	            if (grid.theGrid[MazeWindow.thePlayer.getPosition()[0]][MazeWindow.thePlayer.getPosition()[1] + 1].checkHere()) {
	                MazeWindow.thePlayer.moveRight();
	            	grid.played[MazeWindow.thePlayer.getPosition()[0]][MazeWindow.thePlayer.getPosition()[1] + 1] = true;
	            	grid.played[MazeWindow.thePlayer.getPosition()[0] - 1][MazeWindow.thePlayer.getPosition()[1]] = true;
	            	grid.played[MazeWindow.thePlayer.getPosition()[0] + 1][MazeWindow.thePlayer.getPosition()[1]] = true;
	            }
	            gridCanvas.repaint();
	            break;
	        case KeyEvent.VK_DOWN:
	            if (grid.theGrid[MazeWindow.thePlayer.getPosition()[0] + 1][MazeWindow.thePlayer.getPosition()[1]].checkHere()) {
	                MazeWindow.thePlayer.moveDown();
	            	if (MazeWindow.thePlayer.getPosition()[0] < grid.size[0] - 1) {
	            		grid.played[MazeWindow.thePlayer.getPosition()[0] + 1][MazeWindow.thePlayer.getPosition()[1]] = true;
	            	}
	            	grid.played[MazeWindow.thePlayer.getPosition()[0]][MazeWindow.thePlayer.getPosition()[1] - 1] = true;
	            	grid.played[MazeWindow.thePlayer.getPosition()[0]][MazeWindow.thePlayer.getPosition()[1] + 1] = true;
	            }
	            gridCanvas.repaint();
	            break;
	        }
	    	if (MazeWindow.thePlayer.getPosition()[0] == grid.size[0] - 1) {
	    		score = new ScoreDialog(this);
	    		for (int i = 1; i < grid.size[0] - 1; i++)
	                for (int j = 1; j < grid.size[1] - 1; j++)
	                	grid.played[i][j] = true;
	    		gridCanvas.repaint();
	    		score.setVisible(true);
	    	}
		}
	}

	//Methods below are required for the implemented interfaces but have no function
	public void windowOpened(WindowEvent e) {}
	public void windowClosed(WindowEvent e) {}
	public void windowIconified(WindowEvent e) {}
	public void windowDeiconified(WindowEvent e) {}
	public void windowActivated(WindowEvent e) {}
	public void windowDeactivated(WindowEvent e) {}
	public void keyReleased(KeyEvent arg0) {}
	public void keyTyped(KeyEvent arg0) {}
}
