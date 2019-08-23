String  dateString = "15-11-2019";
SimpleDateFormat formatter = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);// Definir le format de la date
Date date = formatter.parse(dateString); //convertir String en Date
Calendar calendar = Calendar.getInstance();
calendar.setTime(date); // convertir Date en Calendar 
calendar.add(Calendar.DATE,1); // Ajouter 1 jour à la date actuelle
