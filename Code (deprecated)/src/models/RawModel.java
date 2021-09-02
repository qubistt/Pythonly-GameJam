package models;

//Project name
public class RawModel {
	
	//Variables for 3D data
	private int vaoID;
	private int vertexCount;
	
	//Using this keyword to eliminate confusion between class and attribs
	public RawModel(int vaoID, int vertexCount) {
		
		this.vaoID = vaoID;
		this.vertexCount = vertexCount;
		
	}
	
	//Getters
	public int getVaoID() {
		return vaoID;
	}

	public int getVertexCount() {
		return vertexCount;
	}
	
	
}
