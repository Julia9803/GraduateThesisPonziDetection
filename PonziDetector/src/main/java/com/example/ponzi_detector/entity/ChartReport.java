package com.example.ponzi_detector.entity;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.io.Serializable;

@Entity
public class ChartReport implements Serializable {
    public ChartReport() {}

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int chartId;
    private String featureName;
    private String featureImportance;

    public int getChartId() {
        return chartId;
    }

    public void setChartId(int chartId) {
        this.chartId = chartId;
    }

    public String getFeatureImportance() {
        return featureImportance;
    }

    public void setFeatureImportance(String featureImportance) {
        this.featureImportance = featureImportance;
    }

    public String getFeatureName() {
        return featureName;
    }

    public void setFeatureName(String featureName) {
        this.featureName = featureName;
    }
}
