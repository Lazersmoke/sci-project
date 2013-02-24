public class Vm{
	public static void main(String args[]){
		float x = 0.0F;
		float y = 0.1F;
		while(y<500000.1F){
			y+=0.1F;
			x+=0.1F;
		}
		java.lang.System.out.println(x);
	}
}
