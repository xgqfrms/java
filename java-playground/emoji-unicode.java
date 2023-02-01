// java & unicode & emoji
/*
 * https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=java
 *
 * https://www.cnblogs.com/xgqfrms/p/17082942.html
 *
 */

public class HelloWorld {
  public static void main(String []args) {
    String s = "java";
    System.out.println(s.length());
    // Unicode length
    System.out.println("Hello World".length());
    System.out.println("✅".length());
    System.out.println("👨🏻‍💻".length());
    String str = "abc";
    for(int i=0; i<str.length(); i++){
      char ch = str.charAt(i);
      System.out.println(ch);
    }
    String emoji = "👨🏻‍💻";
    for(int i=0; i< emoji.length(); i++){
      char c = emoji.charAt(i);
      System.out.println(c);
    }
  }
}

/*

4
11
1
7
a
b
c
?
?
?
?
‍
?
?


*/
