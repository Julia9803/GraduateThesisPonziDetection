package com.example.ponzi_detector.python;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class FeatureExtractionTest {

    @Test
    void setFeature() {
        FeatureExtraction featureExtraction = new FeatureExtraction();
        featureExtraction.setFeature("ALL",3);
    }
}