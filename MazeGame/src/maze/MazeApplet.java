package maze;

import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.MediaTracker;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

public class MazeApplet extends Applet implements Runnable, MouseListener {
	private static final long serialVersionUID = 1849599308801362725L;
	
	//lets do some double buffering.
	private Image offIm = null;
	private Graphics offGraphics = null;
	private int currentImage;
	private MazeWindow window;

	public void init() {
		Thread card_loader = new Thread(this);
		card_loader.start();
		window = new MazeWindow();
		addMouseListener(this);
	}
  
	public void paint(Graphics g) {
		update(g);
	}
  
	public void update(Graphics g) {
		//lets sort out double buffering
		if(offGraphics == null) {
			offIm = createImage(getSize().width, getSize().height);
			offGraphics = offIm.getGraphics();
		}
		//draw buffered image.
		g.drawImage(offIm,0,0,this);
	}

	public void run() {
		String image_prefix = "../images/";
		String image_suffix = ".gif";
		
		Image unknownCell = getImage(getCodeBase(),image_prefix + "unknown" + image_suffix);
		Image openCell = getImage(getCodeBase(),image_prefix + "open" + image_suffix);
		Image wallCell = getImage(getCodeBase(),image_prefix + "wall" + image_suffix);
		Image playerCell = getImage(getCodeBase(),image_prefix + "player" + image_suffix);

		Image[] images = {unknownCell,openCell,wallCell,playerCell};
		
		MazeWindow msw = new MazeWindow();
		MediaTracker mt = new MediaTracker(msw);
		
		for(currentImage = 0; currentImage < images.length; currentImage ++) {
			mt.addImage(images[currentImage],currentImage);
			try {
				mt.waitForID(currentImage);
				repaint();
			}
			catch (InterruptedException ioe) {
				System.out.println("Interrupted loading images..");
			}
		}
		if(window == null)
		{
			window = new MazeWindow();
		}
		window.init(images);
		repaint();
	}
	
	public void mousePressed(MouseEvent evt) { //Required by Sun's own Java implementation
      requestFocus();
   }
   
   public void mouseEntered(MouseEvent evt) {}
   public void mouseExited(MouseEvent evt) {}
   public void mouseReleased(MouseEvent evt) {}
   public void mouseClicked(MouseEvent evt) {}
}  
  
    
      

