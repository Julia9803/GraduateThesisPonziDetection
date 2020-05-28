package com.example.ponzi_detector.service.impl;

import com.example.ponzi_detector.dao.ChartReportRepository;
import com.example.ponzi_detector.dao.ReportRepository;
import com.example.ponzi_detector.dao.SingleReportRepository;
import com.example.ponzi_detector.entity.ChartReport;
import com.example.ponzi_detector.entity.Report;
import com.example.ponzi_detector.entity.SingleReport;
import com.example.ponzi_detector.service.ReportService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ReportServiceBean implements ReportService {
    @Autowired
    ReportRepository reportRepository;
    @Autowired
    ChartReportRepository chartReportRepository;
    @Autowired
    SingleReportRepository singleReportRepository;


    @Override
    public Report getReport() {
        return reportRepository.findByReportId(0);
    }

    @Override
    public boolean getSingleReport(String address) {
        try {
            SingleReport singleReport = singleReportRepository.getByAddress(address);
            if(singleReport.getIsPozi() == 1)
                return true;
            else
                return false;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    @Override
    public ChartReport getChartReport() {
        return chartReportRepository.getByChartId(0);
    }

    @Override
    public Report getConfigReport() {
        return null;
    }
}
