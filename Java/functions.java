function findLargest(numbers) {
    var max = numbers[0];
    numbers.forEach(function(value){
        max=(max>value)?max:value;
    });
    return max;
}

static boolean dichotomie(int[] ints, int k) {
		boolean result = false;
		int min = 0, max = ints.length-1, middle = (min+max)/2;
		if(ints.length == 0 || k<ints[min] || k>ints[max])
		    return false;
		    
		while(min<middle && middle<max)
		{
		    if(ints[min]==k || ints[middle]==k || ints[max]==k)
		        return true;
	        else
	        {
	            if(k<ints[middle])
	            {
	                max = middle;
	                middle = (min+max)/2;
	            }
	            else if(k>ints[middle])
	            {
	                min = middle;
	                middle = (min+max)/2;
	            }
	        }
		}
		return false;
	}


	public static String getTextFormate(String old, int n)
	{
		String transform = old.replace(" ", "");
		String t2="";
		for (int i=0;i<transform.length();i++)
		{
			if(i!=0 && i%n==0)
				t2 += "\n"+transform.charAt(i);
			else 
				t2 += transform.charAt(i);
		}
		return t2;
	}
