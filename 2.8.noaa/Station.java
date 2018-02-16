package Station;

import java.io.*;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class Station {

    public static void main() throws IOException{

        String localSrc = "/test/isd-history.txt";
        Path path d = new Path(localSrc);
        
        //Open the file
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(conf);
        FSDataInputStream in = fs.open(path);

        try {

            InputStreamReader isr = new InputStreamReader(in);
            BufferedReader br = new BufferedReader(isr);
            
            int n = 0;
            br.readline();
            
            while (br != null) {
                
                n = n + 1
                if (n > 22) {
                    
                    // Process of the current line
                    System.out.println(br.readLine().substring(0, 7) + " " + br.readLine().substring(13, 42) + " " + br.readLine().substring(43, 45) + " " + br.readLine().substring(74, 81));
                    // go to the next line
                }
                br.readLine();
            }
        }

        finally {
            //close the file
            in.close();
            fs.close();
        }
    }
}

