package com.example.ponzi_detector.python;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Properties;

import org.python.core.PyFunction;
import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;


public class FeatureExtraction {

    public void setFeature(String method, int n) {
//        String method = "ALL";
//        int n = 1;
//        String[] args = new String[] {"python","/Users/julia98/git/BachelorDree/ponzi_detection",method,String.valueOf(n)};
//        try {
//            Process process = Runtime.getRuntime().exec(args);
//            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream()));
//            String line = null;
//            while ((line = in.readLine()) != null) {
//                System.out.println(line);
//            }
//            in.close();
//            process.waitFor();
//        } catch (IOException | InterruptedException e) {
//            e.printStackTrace();
//        }


        Properties props = new Properties();
        props.put("python.home", "/Users/julia98/git/BachelorDree/ponzi_detection");
        props.put("python.console.encoding", "UTF-8");
        props.put("python.security.respectJavaAccessibility", "false");
        props.put("python.import.site", "false");

        Properties preprops = System.getProperties();
        PythonInterpreter.initialize(preprops, props, new String[0]);
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.execfile("/Users/julia98/git/BachelorDree/ponzi_detection/model_RF.py");
        PyFunction  func = (PyFunction) interpreter.get("RandomForest", PyFunction.class );
        PyObject pyobj = func.__call__(new PyString(method), new PyInteger(n));
        System.out.println("the anwser is: " + pyobj);

    }
}
