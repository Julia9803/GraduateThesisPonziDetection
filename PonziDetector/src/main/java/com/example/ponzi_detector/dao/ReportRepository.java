package com.example.ponzi_detector.dao;

import com.example.ponzi_detector.entity.Report;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ReportRepository extends CrudRepository<Report,Integer> {
    Report findByReportId(int i);

}
