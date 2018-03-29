package maze;

import java.awt.Button;
import java.awt.Dialog;
import java.awt.Frame;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.Panel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.WindowListener;
import java.awt.event.WindowEvent;
import java.lang.Integer;

public class ScoreDialog extends Dialog implements ActionListener, WindowListener {
	private static final long serialVersionUID = 1121518023267035579L;
	private Button buttonOK = new Button();
	private Integer scoreInt;
	private Frame owner;
	
	public ScoreDialog(Frame owner) {
		super(owner,"Score",true);
		this.owner = owner;
		scoreInt = new Integer(MazeWindow.grid.score());
		buttonOK.setLabel(scoreInt.toString());
		addWindowListener(this);
		Panel inner = new Panel();
		Panel upper = new Panel();
		Panel outer = new Panel();
		GridBagLayout splayout = new GridBagLayout();
		GridBagConstraints gbc = new GridBagConstraints();
		inner.setLayout(new GridLayout(1,1));
		outer.setLayout(new GridLayout(3,1));
		setResizable(false);
		inner.add(buttonOK);
		outer.add(upper);
		outer.add(inner);
		gbc.gridy = 1;
		splayout.setConstraints(outer,gbc);
		setLayout(splayout);
		add(outer);
		validate();
		pack();
		setVisible(false);
		buttonOK.addActionListener(this);
		addWindowListener(this);
	}

	public void setVisible(boolean visible)	{
		if(visible)	{
			setLocation(owner.getLocation().x + owner.getSize().width/2 - getSize().width/2,owner.getLocation().y + owner.getSize().height/2 - getSize().height/2);
			super.setVisible(visible);
		}
	}
	
	public void actionPerformed(ActionEvent e) {
		super.setVisible(false);
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

