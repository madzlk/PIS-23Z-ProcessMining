
CREATE TABLE log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    incident_id VARCHAR(255),
    DateStamp TIMESTAMP,
    incident_activity_type VARCHAR(255)
);

INSERT INTO log (incident_id, DateStamp, incident_activity_type) VALUES ('IM0000004', '2013-01-07 08:17:17', 'Reassignment');
INSERT INTO log (incident_id, DateStamp, incident_activity_type) VALUES ('IM0000005', '2014-02-18 08:17:17', 'Operator Update');
INSERT INTO log (incident_id, DateStamp, incident_activity_type) VALUES ('IM0000006', '2013-09-29 08:17:17', 'Status Change');
INSERT INTO log (incident_id, DateStamp, incident_activity_type) VALUES ('IM0000007', '2015-06-15 08:17:17', 'Reassignment');
INSERT INTO log (incident_id, DateStamp, incident_activity_type) VALUES ('IM0000006', '2017-01-17 08:17:17', 'Operator Update');
INSERT INTO log (incident_id, DateStamp, incident_activity_type) VALUES ('IM0000006', '2018-01-09 08:17:17', 'Reassignment');
INSERT INTO log (incident_id, DateStamp, incident_activity_type) VALUES ('IM0000005', '2012-02-01 08:17:17', 'Status Change');
INSERT INTO log (incident_id, DateStamp, incident_activity_type) VALUES ('IM0000007', '2013-05-02 08:17:17', 'Operator Update');
INSERT INTO log (incident_id, DateStamp, incident_activity_type) VALUES ('IM0000004', '2013-11-04 08:17:17', 'Status Change');
