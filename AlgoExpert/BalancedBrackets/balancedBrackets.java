import java.util.*;

class Program {
  public static boolean balancedBrackets(String str) {

  Stack<Character> bracketsStack = new Stack<>();
  

  for(int i =0; i<str.length(); i++){

    if(str.charAt(i) == '(' || str.charAt(i) == '[' || str.charAt(i) == '{'){
      bracketsStack.push(str.charAt(i));
    }else if(str.charAt(i) == ')' || str.charAt(i) == ']' || str.charAt(i) == '}'){
     
      if(bracketsStack.isEmpty()){
        return false;
      }
      char lastBracket = bracketsStack.pop();
      
     
      if(str.charAt(i) != closingBracket(lastBracket)){
        return false;
      }
    }

    
  }  

    if(!bracketsStack.isEmpty()){
      return false;
    }
    
    return true;
  }


  public static char closingBracket(char bracket){

    if(bracket == '('){
      return ')';
    }else if(bracket == '['){
      return ']';
    }else{
      return '}';
    }
    
  }


  public static void main(String[] args) {
    String input = "([])(){}(())()()";
    System.out.println(balancedBrackets(input)); 
    }
  
}

