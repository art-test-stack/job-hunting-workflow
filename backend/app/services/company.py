from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.orm.company import Company

from app.orm.industry import Industry
from app.orm.job_ci import JobCi
from app.orm.company_industry import CompanyIndustry

from app.services.industry import _add_company_industry, _update_company_industries

def _add_company(
        db: Session, 
        name: str, 
        website: str | None = None, 
        industry: list[str] | None = None
    ):
    company = db.query(Company).filter(Company.name == name).first()
    if company:
        return company  # Company already exists

    company = Company(name=name, website=website, industry=industry)
    db.add(company)
    db.commit()
    db.refresh(company)
    if industry:
        for ind in industry:
            _add_company_industry(db, company.id, ind)
    return company

def _get_company_by_name(db: Session, name: str):
    return db.query(Company).filter(Company.name == name).first()

def _update_company(
        db: Session, 
        company_id: str, 
        name: str | None = None, 
        website: str | None = None, 
        industry: list[str] | None = None
    ):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    if name:
        company.name = name
    if website:
        company.website = website
    if industry is not None:
        _update_company_industries(db, company_id, industry)
    db.commit()
    db.refresh(company)
    return company