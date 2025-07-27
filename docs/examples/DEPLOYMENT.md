# Deployment Guide

## Overview
**Application**: [Your Application Name]  
**Version**: [Version Number]  
**Environment**: [Production/Staging]  
**Last Updated**: [Date]  

## Pre-Deployment Checklist

### Code Quality
- [ ] All tests passing (unit, integration, e2e)
- [ ] Code review completed
- [ ] No console errors or warnings
- [ ] Linting passes without errors
- [ ] Type checking passes (if applicable)
- [ ] Security scan completed
- [ ] Performance benchmarks met

### Documentation
- [ ] README.md updated
- [ ] API documentation current
- [ ] Environment variables documented
- [ ] CHANGELOG.md updated
- [ ] Architecture diagram current
- [ ] Deployment runbook updated

### Configuration
- [ ] Environment variables set
- [ ] API keys and secrets configured
- [ ] Database connection strings verified
- [ ] Third-party service integrations configured
- [ ] CORS settings appropriate
- [ ] Rate limiting configured
- [ ] SSL certificates valid

## Deployment Steps

### 1. Backend Deployment

#### Node.js/Express
```bash
# Build application
npm run build

# Run migrations
npm run migrate:prod

# Deploy to service
# Example: Heroku
git push heroku main

# Example: AWS
eb deploy

# Example: Docker
docker build -t app:latest .
docker push registry/app:latest
```

#### Python/FastAPI
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Deploy
# Example: Gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app

# Example: Docker
docker build -t app:latest .
docker run -p 80:8000 app:latest
```

### 2. Frontend Deployment

#### Static Sites (React/Vue/Astro)
```bash
# Build for production
npm run build

# Deploy to CDN
# Example: Netlify
netlify deploy --prod

# Example: Vercel
vercel --prod

# Example: AWS S3 + CloudFront
aws s3 sync dist/ s3://your-bucket --delete
aws cloudfront create-invalidation --distribution-id YOUR_ID --paths "/*"
```

#### Next.js
```bash
# Build application
npm run build

# Deploy
# Example: Vercel (automatic with git push)
git push origin main

# Example: Self-hosted
npm run start

# Example: Docker
docker build -t nextjs-app .
docker run -p 3000:3000 nextjs-app
```

### 3. Database Deployment

#### PostgreSQL
```bash
# Backup existing database
pg_dump -h old_host -U username -d dbname > backup.sql

# Run migrations
npm run migrate:prod

# Verify data integrity
psql -h host -U username -d dbname -c "SELECT COUNT(*) FROM users;"
```

#### MongoDB
```bash
# Backup existing database
mongodump --uri="mongodb://..." --out=backup/

# Apply schema changes (if any)
node scripts/migrate-mongo.js

# Verify collections
mongo mongodb://... --eval "db.getCollectionNames()"
```

## Environment-Specific Configuration

### Production
```env
NODE_ENV=production
API_URL=https://api.yourdomain.com
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
LOG_LEVEL=error
```

### Staging
```env
NODE_ENV=staging
API_URL=https://staging-api.yourdomain.com
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
LOG_LEVEL=debug
```

## Post-Deployment Verification

### Health Checks
- [ ] Application responds to health endpoint
- [ ] Database connections working
- [ ] External API integrations functional
- [ ] Background jobs running
- [ ] WebSocket connections (if applicable)

### Monitoring Setup
- [ ] Application logs visible
- [ ] Error tracking active (Sentry/Rollbar)
- [ ] Performance monitoring enabled
- [ ] Uptime monitoring configured
- [ ] Alerts configured for critical events

### Smoke Tests
```bash
# API endpoints
curl https://api.yourdomain.com/health
curl https://api.yourdomain.com/api/v1/status

# Frontend
curl -I https://yourdomain.com
```

### Load Testing
```bash
# Example with k6
k6 run load-test.js --vus 100 --duration 5m
```

## Rollback Plan

### Immediate Rollback (< 5 minutes)
```bash
# Revert to previous version
# Example: Heroku
heroku rollback

# Example: Kubernetes
kubectl rollout undo deployment/app

# Example: Docker
docker pull registry/app:previous
docker stop app && docker run registry/app:previous
```

### Database Rollback
```bash
# Restore from backup
psql -h host -U username -d dbname < backup.sql

# Or rollback migrations
npm run migrate:rollback
```

## Platform-Specific Guides

### Vercel
1. Connect GitHub repository
2. Configure environment variables
3. Set build command: `npm run build`
4. Deploy with: `git push origin main`

### Heroku
1. Create app: `heroku create app-name`
2. Add buildpacks if needed
3. Set config vars: `heroku config:set KEY=value`
4. Deploy: `git push heroku main`

### AWS
1. Configure AWS CLI
2. Set up Elastic Beanstalk or ECS
3. Configure load balancer
4. Set up RDS for database
5. Configure CloudWatch for monitoring

### Docker/Kubernetes
1. Build image: `docker build -t app:latest .`
2. Push to registry
3. Update k8s manifests
4. Apply: `kubectl apply -f k8s/`

## Security Checklist

- [ ] HTTPS enabled everywhere
- [ ] Security headers configured
- [ ] API rate limiting active
- [ ] Authentication working properly
- [ ] Authorization rules enforced
- [ ] Sensitive data encrypted
- [ ] Secrets not in code repository
- [ ] Dependencies up to date

## Performance Checklist

- [ ] CDN configured for static assets
- [ ] Database queries optimized
- [ ] Caching strategy implemented
- [ ] Image optimization active
- [ ] Compression enabled (gzip/brotli)
- [ ] Lazy loading implemented
- [ ] Bundle size optimized

## Monitoring & Alerts

### Key Metrics to Monitor
- Response time (p50, p95, p99)
- Error rate
- Request rate
- CPU/Memory usage
- Database connection pool
- Queue lengths

### Alert Thresholds
- Error rate > 1%
- Response time p95 > 1s
- CPU usage > 80%
- Memory usage > 90%
- Disk usage > 85%

## Contact Information

### Deployment Team
- **DevOps Lead**: [Name] - [Email]
- **Backend Lead**: [Name] - [Email]
- **Frontend Lead**: [Name] - [Email]

### Emergency Contacts
- **On-Call**: [Phone]
- **Escalation**: [Manager Name] - [Phone]

### External Services
- **Hosting**: [Provider] - [Support Link]
- **Database**: [Provider] - [Support Link]
- **CDN**: [Provider] - [Support Link]

## Troubleshooting

### Common Issues

#### Application Won't Start
1. Check environment variables
2. Verify database connection
3. Check port availability
4. Review application logs

#### Database Connection Failed
1. Verify connection string
2. Check network/firewall rules
3. Confirm database is running
4. Check connection pool settings

#### High Memory Usage
1. Check for memory leaks
2. Review caching strategy
3. Analyze heap dumps
4. Scale horizontally if needed

## Deployment Log

| Date | Version | Deployed By | Notes |
|------|---------|-------------|-------|
| [Date] | [Version] | [Name] | Initial deployment |

---

**Remember**: Always deploy to staging first, verify everything works, then deploy to production!