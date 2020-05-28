package com.example.ponzi_detector.entity;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.io.Serializable;

@Entity
public class Report implements Serializable {

    public Report() {}

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int reportId;
    private String rfPrecision;
    private String rfRecall;
    private String rfF1Score;
    private String xgbPrecision;
    private String xgbRecall;
    private String xgbF1Score;
    private String lgbPrecision;
    private String lgbRecall;
    private String lgbF1Score;

    public int getReportId() {
        return reportId;
    }

    public String getLgbF1Score() {
        return lgbF1Score;
    }

    public String getLgbPrecision() {
        return lgbPrecision;
    }

    public String getLgbRecall() {
        return lgbRecall;
    }

    public String getRfF1Score() {
        return rfF1Score;
    }

    public String getRfPrecision() {
        return rfPrecision;
    }

    public String getRfRecall() {
        return rfRecall;
    }

    public String getXgbF1Score() {
        return xgbF1Score;
    }

    public String getXgbPrecision() {
        return xgbPrecision;
    }

    public String getXgbRecall() {
        return xgbRecall;
    }

    public void setLgbF1Score(String lgbF1Score) {
        this.lgbF1Score = lgbF1Score;
    }

    public void setLgbPrecision(String lgbPrecision) {
        this.lgbPrecision = lgbPrecision;
    }

    public void setLgbRecall(String lgbRecall) {
        this.lgbRecall = lgbRecall;
    }

    public void setReportId(int reportId) {
        this.reportId = reportId;
    }

    public void setRfF1Score(String rfF1Score) {
        this.rfF1Score = rfF1Score;
    }

    public void setRfPrecision(String rfPrecision) {
        this.rfPrecision = rfPrecision;
    }

    public void setRfRecall(String rfRecall) {
        this.rfRecall = rfRecall;
    }

    public void setXgbPrecision(String xgbPrecision) {
        this.xgbPrecision = xgbPrecision;
    }

    public void setXgbF1Score(String xgbF1Score) {
        this.xgbF1Score = xgbF1Score;
    }

    public void setXgbRecall(String xgbRecall) {
        this.xgbRecall = xgbRecall;
    }
}
