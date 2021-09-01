package renderEngine;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
//import buffer
//buffer is just a piece of data
import java.nio.FloatBuffer;
import java.nio.IntBuffer;
import java.util.ArrayList;
import java.util.List;

import org.lwjgl.BufferUtils;
import org.lwjgl.opengl.GL11;
import org.lwjgl.opengl.GL15;
import org.lwjgl.opengl.GL20;
import org.lwjgl.opengl.GL30;
import org.newdawn.slick.opengl.Texture;
import org.newdawn.slick.opengl.TextureLoader;

import models.RawModel;


public class Loader {
	
	//creating lists to manage VAOs and VBOs and textures
	//becomes easier to clear data if put in a list
	private List<Integer> vaos = new ArrayList<Integer>();
	private List<Integer> vbos = new ArrayList<Integer>();
	private List<Integer> textures = new ArrayList<Integer>();
	
	//use the raw model method made in RawModel
	//to initialize the VAO
	//This VAO is used for vertex position, index buffer and texturing
	//and unbind it when done
	public RawModel loadtoVAO(float[] positions, float[] textureCoords, int[] indices) {
		
		int vaoID = createVAO();
		bindIndicesBuffer(indices);
		storeDataInAttribList(0, 3, positions);
		storeDataInAttribList(1, 2, textureCoords);
		unbindVAO();
		//Raw model needs length of Index Buffer
		return new RawModel(vaoID, indices.length);
		
	}
	
	public int loadTexture(String fileName) {
		
		Texture texture = null;
		try {
			texture = TextureLoader.getTexture("PNG", new FileInputStream("res/"+fileName+".png"));
		} catch (FileNotFoundException e) {
			
			e.printStackTrace();
		} catch (IOException e) {
			
			e.printStackTrace();
		}
		int textureID = texture.getTextureID();
		textures.add(textureID);
		return textureID;
		
	}
	
	
	//Cleaning up, deleting info from lists of VAOs and VBOs
	public void CleanUp() {
		
		//Deleting VAOs made in the list
		for(int vao:vaos) {
			GL30.glDeleteVertexArrays(vao);
		}
		
		//Deleting VBOs made in the list
		for(int vbo:vbos) {
			GL15.glDeleteBuffers(vbo);
		}
		//Deleting textures from the list
		for(int texture:textures) {
			GL11.glDeleteTextures(texture);
		}
		
	}	
	
	//This is the method used in 'public RawModel' above
	//To initialize a VAO and create a blank ID
	private int createVAO() {
		int vaoID = GL30.glGenVertexArrays();
		vaos.add(vaoID);
		GL30.glBindVertexArray(vaoID);
		return vaoID;
	}
	
	//Finally, store data in a VBO which will be added in a VAO
	//This is for vertices
	private void storeDataInAttribList(int attributeNumber, int coordinateSize, float data[]) {
			
		//Initialize a VBO
		int vboID = GL15.glGenBuffers();
			
		//Add it to the list of death
		vbos.add(vboID);
			
		//Bind it so you can use it
		GL15.glBindBuffer(GL15.GL_ARRAY_BUFFER, vboID);
			
		//Set the float buffer data to the VBO data
		FloatBuffer buffer = storeDataInFloatBuffer(data);
			
		//Give some rules
		GL15.glBufferData(GL15.GL_ARRAY_BUFFER, buffer, GL15.GL_STATIC_DRAW);
		GL20.glVertexAttribPointer(attributeNumber, coordinateSize, GL11.GL_FLOAT,false,0,0);
		GL15.glBindBuffer(GL15.GL_ARRAY_BUFFER, 0);
			
	}
	
	//Unbind VAO after done using
	private void unbindVAO() {
		GL30.glBindVertexArray(0);
	}
	
	//Setting up Index Buffer
	private void bindIndicesBuffer(int [] indices) {
		int vboID = GL15.glGenBuffers();
		vbos.add(vboID);
		GL15.glBindBuffer(GL15.GL_ELEMENT_ARRAY_BUFFER, vboID);
		IntBuffer buffer = storeDataInIntBuffer(indices);
		GL15.glBufferData(GL15.GL_ELEMENT_ARRAY_BUFFER, buffer, GL15.GL_STATIC_DRAW);
		
	}
	
	//The data has to be stored in an INT buffer first
	private IntBuffer storeDataInIntBuffer(int[] data) {
		
		//Use utils to create a new buffer
		IntBuffer buffer = BufferUtils.createIntBuffer(data.length);
		
		//Put the data and flip it to READ mode
		buffer.put(data);
		buffer.flip();
		
		//Return new data
		return buffer;
	}
	
	
	//The data has to be stored in a float buffer first
	//This is for vertices
	private FloatBuffer storeDataInFloatBuffer(float[] data) {
		
		//Create a float buffer to store data in
		FloatBuffer buffer = BufferUtils.createFloatBuffer(data.length);
		buffer.put(data);
		
		//To flip it between read/write mode
		//So its ready to be READ from 
		buffer.flip();
		
		//Return new value
		return buffer;
	}
	
	
}
