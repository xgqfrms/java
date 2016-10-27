public class Main {
    public static void main(String[] args) {
        String str = "Failure is probably the fortification in your pole. It is like a peek your wallet as the thief, when you are thinking how to spend several hard-won lepta, when you are wondering whether new money, it has laid background. Because of you, then at the heart of the most lax, alert, and most low awareness, and left it godsend failed.";
         
        String[] words = str.split("[^\\w\\-]+");
        for(String w : words) {
            System.out.println(w);
        }
    }
}