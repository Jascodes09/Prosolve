import javax.swing.*;
import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DigitalClock {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Digital Clock");
        JLabel timeLabel = new JLabel();
        timeLabel.setFont(new Font("Verdana", Font.BOLD, 40));
        timeLabel.setHorizontalAlignment(SwingConstants.CENTER);

        frame.add(timeLabel);
        frame.setSize(400, 150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        // Clock update loop
        while (true) {
            Date now = new Date();
            SimpleDateFormat formatter = new SimpleDateFormat("HH:mm:ss");
            timeLabel.setText(formatter.format(now));

            try {
                Thread.sleep(1000); // Update every second
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
