package myFirst;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class Fichier {

	public static String getPath(String name, String root) {
		boolean found = false;
		List<String> path = new ArrayList();
		getPathAux(root, name, found, path);

		if (path.size() == 1)
			return null;
		else {
			String chemin = path.get(0).toString();
			for (int i = 1; i < path.size(); i++) {
				chemin += "/" + path.get(i);
			}
			return chemin;
		}
	}

	private static void getPathAux(String currentFolder, String name, boolean found, List<String> path) {
		if (!found) {
			path.add(currentFolder);
			//System.out.println(merge(path));
			File repertoire = new File(merge(path));
			//System.out.println(merge(path));
			File[] fichiers = repertoire.listFiles();
			for (int i = 0; i < fichiers.length; i++) {
				if(found) break;
				File fichierCourant = fichiers[i];
				//System.out.println(i+"/"+fichierCourant.getName()+"/"+path.size()+"/"+found+"==>"+merge(path));
				if (fichierCourant.isFile()) {
					if (fichierCourant.getName().equals(name)) {
						found = true;
					}
				} else if (fichierCourant.isDirectory()) {
					//System.out.println(fichierCourant.toString());
					getPathAux(fichierCourant.getName(), name, found, path);
					path.remove(path.size()-1);
				}
				
			}
		}

	}
	
	
	private static String merge(List<String> chemin)
	{
		
		if(chemin.size()!=0)
		{
			String result = chemin.get(0);
			for(int i=1; i<chemin.size();i++)
			{
				result+="/"+chemin.get(i);
			}
			return result;
		}
		else
		{
			return "";
		}
		
	}

}
