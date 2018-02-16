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
            String line = br.readline();
            
            while (br != null) {
                
                n = n + 1
                if (n > 22) {     
                    System.out.println(line.substring(0, 7) + " " + line.substring(13, 42) + " " + line.substring(43, 45) + " " + line.substring(74, 81));
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

