package BALOCA;


public class W2E2BALOCA {

	public static void main(String[] args) {
		
		int[][] baloca_one = {
				{0, 1, 1, 0},
				{1, 1, 0, 0},
				{0, 0, 1, 1},
				{1, 1, 0, 0},
		};
		
		int balocazeros = 0;
		int balocaones = 0;
		
		for (int row = 0; row < 4; row++)
		{
			int rowones = 0;
			for (int col = 0; col < baloca_one[row].length; col++) {
				if (baloca_one[row][col] == 0) {
						balocazeros++;
				} else {
					balocaones++;
					rowones++;
				}
			}
			
			System.out.println("Row " + row + " has " + rowones + " ones.");
		}
		
		for (int row = 0; row < 4; row++)
		{
			int rowzeros = 0;
			for (int col = 0; col < baloca_one[row].length; col++) {
				if (baloca_one[row][col] == 1) {
						balocaones++;
				} else {
					balocazeros++;
					rowzeros++;
				}
			}
			System.out.println("Row " + row + " has " + rowzeros + " zeros.");
		
	}
	}
}
