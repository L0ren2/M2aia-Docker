if (!require("Cardinal"))
       if (!requireNamespace("BiocManager", quietly = TRUE))
              install.packages("BiocManager")
       BiocManager::install("Cardinal")

library("Cardinal")

fcThreshold <- 1
pThreshold  <- 0.05

roiSel <- df_fil %>% 
  group_by(ROI, label) %>% 
  summarise(nPixel = n(),
            labelROI = first(labelROI)) %>% 
  separate(ROI, into = c(NA, "treat", "cell", "rep"), remove = FALSE) %>% 
  ungroup() %>%
  mutate(idx = row_number()) %>% 
  filter(treat == "CTRL", 
         nPixel > 5, 
         cell %in% c("CCD", "HT")) %>%
  pull(labelROI)

dfPlot <- intmat_fil %>%
  as_tibble(rownames = "ROI") %>%
  filter(ROI %in% roiSel) %>%
  gather(mz, int, -ROI) %>%
  separate(ROI, into = c("cluster", NA, "treat", "cell", "rep")) %>%
  group_by(cell, mz) %>%
  summarise(int = list(int)) %>%
  spread(cell, int) %>%
  group_by(mz) %>%
  mutate(pval = t.test(unlist(CCD), unlist(HT))$p.value,
         log2FC = log2(mean(unlist(CCD))/mean(unlist(HT)))) %>%
  ungroup() %>%
  mutate(padj = p.adjust(pval, method = "BH", n = dim(intmat_fil)[2]),
         sig = padj < pThreshold & abs(log2FC) > fcThreshold,
         label = ifelse(sig, round(as.numeric(mz), 2), NA)) 


ggplot(dfPlot, aes(x = log2FC,
           y = -log10(padj),
           col = sig,
           label = label)) +
geom_point(alpha = 0.75, show.legend = FALSE) +
geom_hline(aes(yintercept = -log10(pThreshold)), 
           linetype = "dashed", alpha = 0.5) +
geom_vline(aes(xintercept = fcThreshold),
           linetype = "dashed", alpha = 0.5) +
geom_vline(aes(xintercept = -fcThreshold),
           linetype = "dashed", alpha = 0.5) +
  geom_text(hjust = 1, vjust = 1, 
            check_overlap = TRUE, 
            col = "black") +
theme_minimal(base_size = 16) +
labs(x = "log2(CCD / HT)",
     y = "-log10(adj. p-value)") 
  