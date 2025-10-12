from sqlalchemy.orm import Session

from app.orm.industry import Industry
from app.orm.job_ci import JobCi
from app.orm.company_industry import CompanyIndustry


def _add_job_industry(
        db: Session,
        job_id: str,
        company_id: str,
        industry: str
    ):
    industry_obj = db.query(Industry).filter(Industry.name == industry).first()
    if not industry_obj:
        industry_obj = Industry(name=industry)
        db.add(industry_obj)
        db.commit()
        db.refresh(industry_obj)
    company_industry = db.query(CompanyIndustry).filter(
        CompanyIndustry.company_id == company_id,
        CompanyIndustry.industry_id == industry_obj.id
    ).first()
    if not company_industry:
        company_industry = CompanyIndustry(company_id=company_id, industry_id=industry_obj.id)
        db.add(company_industry)
        db.commit()
        db.refresh(company_industry)
    job_ci = JobCi(job_id=job_id, company_industry_id=company_industry.id, company_id=company_id)
    db.add(job_ci)
    db.commit()
    db.refresh(job_ci)
    return job_ci

def _add_company_industry(
        db: Session,
        company_id: str,
        industry: str
    ):
    industry_obj = db.query(Industry).filter(Industry.name == industry).first()
    if not industry_obj:
        industry_obj = Industry(name=industry)
        db.add(industry_obj)
        db.commit()
        db.refresh(industry_obj)
    company_industry = db.query(CompanyIndustry).filter(
        CompanyIndustry.company_id == company_id,
        CompanyIndustry.industry_id == industry_obj.id
    ).first()
    if not company_industry:
        company_industry = CompanyIndustry(company_id=company_id, industry_id=industry_obj.id)
        db.add(company_industry)
        db.commit()
        db.refresh(company_industry)
    return company_industry

def update_job_industries(
        db: Session,
        job_id: str,
        company_id: str,
        industries: list[str]
    ):
    db.query(JobCi).filter(JobCi.job_id == job_id).delete()
    db.commit()
    for industry in industries:
        _add_job_industry(db, job_id, company_id, industry)

def _update_company_industries(
        db: Session,
        company_id: str,
        industries: list[str]
    ):
    db.query(CompanyIndustry).filter(CompanyIndustry.company_id == company_id).delete()
    db.commit()
    for industry in industries:
        _add_company_industry(db, company_id, industry)

def _get_job_industries(db: Session, job_id: str):
    industries = (
        db.query(Industry)
        .join(CompanyIndustry, CompanyIndustry.industry_id == Industry.id)
        .join(JobCi, JobCi.company_industry_id == CompanyIndustry.id)
        .filter(JobCi.job_id == job_id).all()
    )
    print("industries", industries)
    return set([ind.name for ind in industries])

def _get_company_industries(db: Session, company_id: str):
    industries = (
        db.query(
            Industry
        ).join(CompanyIndustry).filter(CompanyIndustry.company_id == company_id).all()
    )
    return set([ind.name for ind in industries])
