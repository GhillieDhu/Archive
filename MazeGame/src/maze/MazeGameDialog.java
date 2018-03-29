package maze;

import java.awt.Button;
import java.awt.Dialog;
import java.awt.Frame;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.Label;
import java.awt.Panel;
import java.awt.TextField;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.WindowListener;
import java.awt.event.WindowEvent;

public class MazeGameDialog extends Dialog implements ActionListener, WindowListener {
	private static final long serialVersionUID = 1121518023267035579L;
	private Button buttonOK = new Button("OK");
	private Button buttonCancel = new Button("Cancel");
	private final Label labelWidth = new Label("Width");
	private final Label labelHeight = new Label("Height");
	private TextField textWidth;
	private TextField textHeight;
	private int width;
	private int height;
	private int defaultWidth;
	private int defaultHeight;
	private Frame owner;
	
	public MazeGameDialog(Frame owner, int defaultHeight, int defaultWidth) {
		super(owner,"Custom Field",true);
		this.owner = owner;
		this.width = defaultWidth;
		this.height = defaultHeight;
		addWindowListener(this);
		textWidth = new TextField(""+defaultWidth);
		textHeight = new TextField(""+defaultHeight);
		this.defaultWidth = defaultWidth;
		this.defaultHeight = defaultHeight;
		Panel sp = new Panel();
		Panel pl = new Panel();
		Panel pr = new Panel();
		GridBagLayout splayout = new GridBagLayout();
		GridBagConstraints gbc = new GridBagConstraints();
		sp.setLayout(splayout);
		pl.setLayout(new GridLayout(2,1));
		pr.setLayout(new GridLayout(2,0,10,10));
		gbc.weightx += 10;
		gbc.weighty += 10;
		gbc.gridwidth = GridBagConstraints.RELATIVE;
		setResizable(false);
		pl.add(labelWidth);
		pl.add(textWidth);
		pl.add(labelHeight);
		pl.add(textHeight);
		pr.add(buttonOK);
		pr.add(buttonCancel);
		splayout.setConstraints(pl,gbc);
		sp.add(pl);
		gbc.gridwidth=GridBagConstraints.REMAINDER;
		splayout.setConstraints(pr,gbc);
		sp.add(pr);
		splayout=new GridBagLayout(); 
		gbc=new GridBagConstraints();
		setLayout(splayout);
		gbc.ipadx += 20;
		gbc.ipady += 10;
		splayout.setConstraints(sp,gbc);
		add(sp);
		validate();
		pack();
		setVisible(false);
		buttonOK.addActionListener(this);
		buttonCancel.addActionListener(this);
		addWindowListener(this);
	}

	public void setVisible(boolean visible)	{
		if(visible)	{
			setLocation(owner.getLocation().x + owner.getSize().width/2 - getSize().width/2,owner.getLocation().y + owner.getSize().height/2 - getSize().height/2);
			super.setVisible(visible);
		}
	}
	
	public int getWidth() {
		return width;
	}
	
	public int getHeight() {
		return height;
	}

	public void actionPerformed(ActionEvent e) {
		if(e.getSource().equals(buttonOK)) {
			try {
				width = Integer.parseInt(textWidth.getText());
			}
			catch(NumberFormatException nfe) {
				width = defaultWidth;
			}
			width = (width > Grid.BASE_SIZE * 6) ? Grid.BASE_SIZE * 6 : width;
			textWidth.setText(""+width);
			try {
				height= Integer.parseInt(textHeight.getText());
			}
			catch(NumberFormatException nfe) {
				height= defaultHeight;
			}
			height = (height > Grid.BASE_SIZE * 4) ? Grid.BASE_SIZE * 4 : height;
			textHeight.setText(""+height);
			super.setVisible(false);
		}
		else { //since only the 2 buttons registered, it's an if/else...
			super.setVisible(false);
		}
	}
	
	public void windowOpened(WindowEvent e) {}

	public void windowClosing(WindowEvent e) {
		dispose();
	}

	public void windowClosed(WindowEvent e) {}

	public void windowIconified(WindowEvent e) {}

	public void windowDeiconified(WindowEvent e) {}

	public void windowActivated(WindowEvent e) {}

	public void windowDeactivated(WindowEvent e) {}
}

