package com.example.ponzi_detector.dao;

import com.example.ponzi_detector.entity.ChartReport;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ChartReportRepository extends CrudRepository<ChartReport,Integer> {
    ChartReport getByChartId(int i);

}
