package com.example.ponzi_detector.controller;

import com.example.ponzi_detector.entity.ChartReport;
import com.example.ponzi_detector.entity.Report;
import com.example.ponzi_detector.service.impl.ReportServiceBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class ReportController {

    @Autowired
    ReportServiceBean reportServiceBean;

//    @RequestMapping("/")
//    public String index() {
//        return "index.html";
//    }

    @RequestMapping(value = "/report", method = RequestMethod.GET)
    @CrossOrigin("http://localhost:8080")
    public Report getReport() {
        return reportServiceBean.getReport();
    }

    @RequestMapping(value = "/singleReport",method = RequestMethod.GET)
    @CrossOrigin("http://localhost:8080")
    public boolean getSingleReport(@RequestParam("address") String address) {
        return reportServiceBean.getSingleReport(address);
    }

    @RequestMapping(value = "/chartReport", method = RequestMethod.GET)
    @CrossOrigin("http://localhost:8080")
    public ChartReport getChartReport() {
        return reportServiceBean.getChartReport();
    }

    @RequestMapping(value = "/configReport", method = RequestMethod.GET)
    @CrossOrigin("http://localhost:8080")
    public Report getConfigReport() {
        return reportServiceBean.getConfigReport();
    }
}
