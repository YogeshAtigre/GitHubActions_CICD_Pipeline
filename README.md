# Step-by-Step Guide: CI/CD Pipeline for Flask App Using GitHub Actions 

This guide walks you through setting up a **CI/CD pipeline** for a **Flask application** using **GitHub Actions**.

---

# 1. Setup GitHub Repository
# 1.1 Create or Use an Existing Flask Repository
- If you don’t have a repository yet, create one on GitHub.
- Clone it locally:
  ```bash
  git clone https://github.com/YogeshAtigre/Python.git
  cd flask-app
  ```

- Ensure your repository has the following branches:
  ```bash
  git checkout -b main
  git checkout -b staging
  git push origin main
  git push origin staging
  ```

**Example Flask Application Repository:**  
[Sample Flask App](https://github.com/YogeshAtigre/Python/main) (You can fork this or create a new one)

---

## **2. Create GitHub Actions Workflow**
### **2.1 Add Workflow Directory**
Inside your repository, create the `.github/workflows` directory:
```bash
mkdir -p .github/workflows
```

### **2.2 Create the Workflow File**
Create a **`ci-cd-pipeline.yml`** inside `.github/workflows/`:
---

## 3. Configure GitHub Secrets
To store sensitive information, go to **GitHub Repository → Settings → Secrets and Variables → Actions → New Repository Secret** and add:
- `STAGING_SERVER`: IP address or domain of the staging server.
- `PROD_SERVER`: IP address or domain of the production server.
- `SSH_USER`: The username for SSH access.
- `SSH_KEY`: The private SSH key used to connect.

--

## Workflow Overview
1. **Build & Test**: Runs when code is pushed to `main` or `staging`.
2. **Deploy to Staging**: Triggers when pushing to `staging` branch.
3. **Deploy to Production**: Deploys when a release is published.

## Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/flask-app.git
   cd flask-app
   ```
2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run tests:
   ```bash
   pytest
   ```
4. Push to `staging` for testing:
   ```bash
   git checkout -b staging
   git push origin staging
   ```
5. To deploy to production, create a GitHub release.

## Environment Variables
Set the following GitHub secrets for deployment:
- `STAGING_SERVER`
- `PROD_SERVER`
- `SSH_USER`
- `SSH_KEY`

## Monitoring Workflow
Check workflow runs in **GitHub → Actions**.
---
## **5. Test and Validate**
### **5.1 Push Code to Trigger Workflow**
```bash
git add .
git commit -m "Initial commit with GitHub Actions CI/CD"
git push origin main
```

### **5.2 Verify Workflow Runs**
Go to **GitHub → Your Repository → Actions** to check the progress.

### **5.3 Deploy to Staging**
```bash
git checkout staging
git merge main
git push origin staging
```

### **5.4 Deploy to Production**
1. Go to **GitHub → Releases → New Release**.
2. Create a release and publish it.
3. GitHub Actions will trigger the deployment.
---

## **Conclusion**
You now have a **CI/CD pipeline** that:
✅ **Runs tests** on each push  
✅ **Deploys to staging** on `staging` branch push  
✅ **Deploys to production** when a GitHub release is published  
