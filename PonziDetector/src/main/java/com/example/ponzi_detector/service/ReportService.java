package com.example.ponzi_detector.service;

import com.example.ponzi_detector.entity.ChartReport;
import com.example.ponzi_detector.entity.Report;

public interface ReportService {
    Report getReport();
    boolean getSingleReport(String address);
    ChartReport getChartReport();
    Report getConfigReport();
}
