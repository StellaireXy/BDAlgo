package YearHeightTree;

public class Tree {

	// By using a static method the Tree class is never instantiated but the processing logic is still abstracted away
	public static String getyearheight(String line) {
			
		String[] infotree = line.split(";");
		String year = infotree[5];
		String height = infotree[6];
		
		// Return the line
		return "Year : " + year + '; Height : ' + height + '\n';
	}
}