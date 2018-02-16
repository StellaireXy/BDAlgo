package YearHeightTree;

import java.io.*;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class ReadTree {

    public static void main() throws IOException{

        String localSrc = "/test/arbres.csv";
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
                String yearheight = Tree.getyearheight(line);
                System.out.println(yearheight);
                line = br.readLine();
                
            }
        }

        finally {
            //close the file
            in.close();
            fs.close();
        }
    }
}

