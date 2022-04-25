DROP TABLE IF EXISTS raw;
CREATE TABLE raw (
	
	submission_timestamp timestamp,
	age INT,
	race VARCHAR(255),
	gender VARCHAR(255),
	nationality VARCHAR(255),
	edu_qualification VARCHAR(255),
	job_title VARCHAR(255),
	years_exp DECIMAL(10,2),
	num_jobs INT,
	in_malaysia VARCHAR(255),
	is_remote VARCHAR(255),
	state VARCHAR(255),
	company_type VARCHAR(255),
	industry VARCHAR(255),
	industry_other VARCHAR(255),
	job_specialisation VARCHAR(255),
	job_other VARCHAR(255),
	avg_work_hours DECIMAL(10,2),
	avg_workdays_week DECIMAL(10,2),
	gross_monthly_salary DECIMAL(10,2),
	starting_salary DECIMAL(10,2),
	happy_rating INT,
	job_satisfaction_rating INT,
	thoughts VARCHAR(255),
	email VARCHAR(255),
	code VARCHAR(255),
	id SERIAL PRIMARY KEY
);
INSERT INTO raw (submission_timestamp,age,race,gender,nationality,edu_qualification,job_title,years_exp,num_jobs,in_malaysia,is_remote,state,company_type,industry,industry_other,job_specialisation,job_other,avg_work_hours,avg_workdays_week,gross_monthly_salary,starting_salary,happy_rating,job_satisfaction_rating,thoughts,email,code) VALUES ('12/03/2022 19:48:40','31','Indian','Male','Malaysia','Master''s Degree (Overseas)','Associate ','12','5','Yes','No','Federal Territory of Kuala Lumpur','Small & medium-sized enterprises','Architecture','','Architect','','10','5','10500','3400',4,4,'Have confidence and do not undercut your own salary','','A3TPM9'), ('12/04/2022 19:21:08','32','Chinese','Female','Malaysia','Bachelor''s Degree','Fund Accounting Analyst ll','5','5','Yes','Hybrid','Federal Territory of Kuala Lumpur','Multinational corporation','Financial services/Investment/Banking/Insurance','','Accounting','','9','5','6575','3400',3,3,'','sample@icloud.com','ACD12'), ('12/03/2022 19:18:06','33','Malay','Male','Malaysia','Bachelor''s Degree','Mill engineer','9','2','Yes','Yes','Johor','Private large enterprises (local)','Agriculture/Plantation','','Engineering','','10','6','4500','2600',2,3,'','','ABS12'), ('12/04/2022 19:10:28','29','Chinese','Malaysia','Malaysia','Bachelor''s Degree','Site Quantity Surveyor','2.5','2','Yes','No','Selangor','Small & medium-sized enterprises','Construction','','Quantity Survey','','8','6','5000','2500',2,4,'','sample@yahoo.com','ABD121');
